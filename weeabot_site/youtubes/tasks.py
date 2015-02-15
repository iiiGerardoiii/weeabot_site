from celery.task import task
import requests
import hashlib
import os
import random
import string
from webms.models import Webm

BLOCKSIZE = 65536
MAX_FILESIZE_BYTES = 8000000

'''
to run the celery task daemon in debug, run:
python manage.py celeryd -l info
'''

def generate_new_random_filename(length=5, ext='.webm'):
  filename = None
  while not filename:
    filename = ''.join(random.choice(string.lowercase) for x in range(length))
    #filename += ext
    target = filename + ext
    if Webm.objects.filter(filename=target).count():
      filename = None
  return filename

@task
def new_webm(nick, channel, url, path):
  #first see if this file is not too large by fetching the header only
  header_response = requests.head(url)
  sz = int(header_response.headers['content-length'])
  if sz > MAX_FILESIZE_BYTES:
    #TODO: LOG SOMETHING
    return
  #generate a random string name for this file
  ext = os.path.splitext(url)[1]
  filebase = generate_new_random_filename(length=5, ext=ext)
  filename = filebase + ext

  #download the file
  filepath = os.path.join(path, filename)
  r = requests.get(url)
  with open(filepath, "wb") as code:
    code.write(r.content)
  #form a hash over file contents to uniquely identify it
  hasher = hashlib.md5()
  with open(filepath, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
      hasher.update(buf)
      buf = afile.read(BLOCKSIZE)
  filehash = hasher.hexdigest()

  #does there ALREADY exist an entry in our database with this hash?
  #(i.e. another binary equivalent file?)
  if Webm.objects.filter(filehash=filehash).count():
    os.remove(filepath)
    w = Webm.objects.get(filehash=filehash)
    w.hits = w.hits + 1
    w.save()
    return

  #lastly, generate a thumbnail image
  thumbnail_filename = filebase+"s.jpg"
  thumbnail_filepath = os.path.join(path, thumbnail_filename)
  call = 'ffmpeg -i {filename} -vf scale=128:-1 -vframes 1 {thumb}'.format(filename=filepath,thumb=thumbnail_filepath)
  os.system(call)
  #if the resultant file is not present, it must have been an audio file or something
  if not os.path.isfile(thumbnail_filepath):
    thumbnail_filename='missing.jpg'
  
  w = Webm()
  w.url = url
  w.nick = nick
  w.channel = channel
  w.filename = filename
  w.filehash = filehash
  w.name = ""
  w.desc = ""
  w.thumbnail = thumbnail_filename
  w.save()

