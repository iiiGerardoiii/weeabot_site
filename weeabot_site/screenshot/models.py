from django.db import models

class Screenshot(models.Model):
  '''
  Screenshot captured off live stream
  '''
  channel = models.CharField(max_length=128)
  nick = models.CharField(max_length=128)
  timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
  url = models.CharField(max_length=2048)
  filename = models.CharField(max_length=256)
  name = models.CharField(max_length=256, default="unnamed")
  desc = models.CharField(max_length=2048, default="no description")
  thumbnail = models.CharField(max_length=256, default='missing.jpg')
  
  def __unicode__(self):
    return self.name

  def simple_nick(self):
    return self.nick.split('!')[0]



