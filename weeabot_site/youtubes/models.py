from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
import urlparse

class Tag(models.Model):
  '''A gategory tag for youtubes
  Youtubes can have N tags
  '''
  name = models.CharField(max_length=2048)

  def __unicode__(self):
    return self.name

class Youtube(models.Model):
  '''
  A webm (or gif) scraped off IRC
  '''
  channel = models.CharField(max_length=128)
  nick = models.CharField(max_length=128)
  timestamp = models.DateTimeField(auto_now_add=True)
  url = models.CharField(max_length=2048)
  name = models.CharField(max_length=256, default="")
  desc = models.CharField(max_length=2048, default="no description")
  tags = models.ManyToManyField(Tag, related_name='youtubes', blank=True)
  thumbnail = models.CharField(max_length=1024, default='missing.jpg')
  updated = models.DateTimeField(auto_now=True, default=datetime.now())
  hits = models.IntegerField(default=1)

  class Meta:
    ordering = ['-updated']

  def Name(self):
    if self.name:
      return self.name
    else:
      return self.url

  def __unicode__(self):
    return self.Name()

  def simple_nick(self):
    return self.nick.split('!')[0]

def scrape_youtube_id(url):
  '''get a youtube ID from a url
  '''
  params = urlparse.urlparse(url)
  query = urlparse.parse_qs(params.query)
  if 'v' in query:
    return query['v'][0]
  else:
    return 'None'

@receiver(pre_save, sender=Youtube)
def generate_youtube_id(sender, instance, *args, **kwargs):
    id = scrape_youtube_id(instance.url)
    instance.thumbnail = 'http://img.youtube.com/vi/{id}/default.jpg'.format(id=id)
    instance.name = id 

