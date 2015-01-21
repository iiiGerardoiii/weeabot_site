from django.forms import widgets
from rest_framework import serializers
from webms.models import Webm


class WebmSerializer(serializers.ModelSerializer):
  class Meta:
    model = Webm
    fields = ('id', 'channel', 'nick', 'url', 'filename', 'filehash')