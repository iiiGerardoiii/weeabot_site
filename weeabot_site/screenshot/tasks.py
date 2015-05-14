from celery.task import task
import requests
import hashlib
import os
import random
import string
from screenshot.models import Screenshot
import datetime

BLOCKSIZE = 65536
MAX_FILESIZE_BYTES = 8000000

'''
to run the celery task daemon in debug, run:
python manage.py celeryd -l info
'''

def generate_new_random_filename(length=5, ext='.jpg'):
  filename = None
  while not filename:
    filename = ''.join(random.choice(string.lowercase) for x in range(length))
    #filename += ext
    target = filename + ext
    if Screenshot.objects.filter(filename=target).count():
      filename = None
  return filename

@task
def take_screenshot(nick, channel, url, path):
  print "going to generate random filename..."
  filebase = generate_new_random_filename()
  print "going to screenshot..."
  filename = filebase + ".jpg"
  #take the screenshot
  filepath = os.path.join(path, filename)
  call = 'ffmpeg -ss 00:00:10 -i {url} -r 1 -vframes 1 {filename}'.format(url=url, filename=filepath)
  os.system(call)

  #if we didn't get a thumbnail stream must be down or something
  if not os.path.isfile(filepath):
    return ""

  # generate a thumbnail image
  thumbnail_filename = filebase+"s.jpg"
  thumbnail_filepath = os.path.join(path, thumbnail_filename)
  call = 'ffmpeg -i {filename} -vf scale=256:-1 -vframes 1 {thumb}'.format(filename=filepath,thumb=thumbnail_filepath)
  os.system(call)
  #if the resultant file is not present, it must have been an audio file or something
  if not os.path.isfile(thumbnail_filepath):
    thumbnail_filename=filename

  #tag info with date
  date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  w = Screenshot()
  w.nick = nick
  w.channel = channel
  w.filename = filename
  w.name = url
  w.desc = date
  w.thumbnail = thumbnail_filename
  w.save()

  return filename

