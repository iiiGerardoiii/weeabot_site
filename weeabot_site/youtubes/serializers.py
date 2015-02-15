from django.forms import widgets
from rest_framework import serializers
from youtubes.models import Youtube
from youtubes.models import Tag

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
  def to_representation(self, value):
    return value.name

class YoutubeSerializer(serializers.ModelSerializer):
  tags = TagSerializer(many=True, read_only = True)
  class Meta:
    model = Youtube
    fields = ['id', 'channel', 'nick', 'url', 'name', 'desc', 'tags', 'thumbnail']
