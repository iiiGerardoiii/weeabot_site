from django.db import models

class Webm(models.Model):
  '''
  A webm (or gif) scraped off IRC
  '''
  channel = models.CharField(max_length=128)
  nick = models.CharField(max_length=128)
  timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
  url = models.CharField(max_length=2048)
  filename = models.CharField(max_length=256)
  filehash = models.CharField(max_length=128)
  
  #def __unicode__(self):
  #  return self.text

  #def simple_nick(self):
  #  return self.nick.split('!')[0]
