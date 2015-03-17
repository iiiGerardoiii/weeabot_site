from django.forms import widgets
from rest_framework import serializers
from screenshot.models import Screenshot
#from screenshot.models import Tag

#class TagSerializer(serializers.ModelSerializer):
#  class Meta:
#    model = Tag
#  def to_representation(self, value):
#    return value.name

class ScreenshotSerializer(serializers.ModelSerializer):
  #tags = TagSerializer(many=True, read_only = True)
  class Meta:
    model = Screenshot
    fields = ['id', 'channel', 'nick', 'url', 'filename', 'name', 'desc', 'thumbnail']
