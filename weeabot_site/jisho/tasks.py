from celery.task import task
import requests
import hashlib

BLOCKSIZE = 65536

@task
def add(x, y):
    return x + y

@task
def download(url, path, filename):
  #first fetch our file
  r = requests.get(url)
  with open(filename, "wb") as code:
    code.write(r.content)
  #form a hash over file contents to uniquely identify it
  hasher = hashlib.md5()
  with open(filename, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
  #Put the filename, type, hash etc into our database
  #print("hash: " + hasher.hexdigest())

