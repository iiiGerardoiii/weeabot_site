from django.forms import widgets
from rest_framework import serializers
from webms.models import Webm
from webms.models import Tag

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
  def to_representation(self, value):
    return value.name

class WebmSerializer(serializers.ModelSerializer):
  tags = TagSerializer(many=True, read_only = True)
  class Meta:
    model = Webm
    fields = ['id', 'channel', 'nick', 'url', 'filename', 'name', 'desc', 'tags']
