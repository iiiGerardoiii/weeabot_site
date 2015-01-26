from django.db import models

class Definition(models.Model):
  '''
  Data on a single returned jisho.org lookup
  '''
  channel = models.CharField(max_length=128)
  nick = models.CharField(max_length=128)
  timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
  url = models.CharField(max_length=2048)
  kanji = models.CharField(max_length=32, default='')
  kana = models.CharField(max_length=64, default='')
  romaji = models.CharField(max_length=128, default='')
  text = models.CharField(max_length=256)#english text
  word = models.CharField(max_length=128)
  
  def __unicode__(self):
    return self.text

  def simple_nick(self):
    return self.nick.split('!')[0]
