from django.forms import widgets
from rest_framework import serializers
from jisho.models import Definition


class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = ('id', 'channel', 'nick', 'url', 'text', 'word')