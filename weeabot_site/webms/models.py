from django.db import models

class Tag(models.Model):
  '''A gategory tag for Webms
  Webms can have N tags
  '''
  name = models.CharField(max_length=2048)

  def __unicode__(self):
    return self.name

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
  name = models.CharField(max_length=256)
  desc = models.CharField(max_length=2048)
  tags = models.ManyToManyField(Tag, related_name='webms', blank=True)
  
  def __unicode__(self):
    return self.name

  def simple_nick(self):
    return self.nick.split('!')[0]



