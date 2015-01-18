from django.forms import widgets
from rest_framework import serializers
from jisho.models import Definition


class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = ('channel', 'nick', 'url', 'text', 'word')
'''
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.channel = validated_data.get('channel', instance.channel)
        instance.nick = validated_data.get('nick', instance.nick)
        #instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.url = validated_data.get('url', instance.url)
        instance.text = validated_data.get('text', instance.text)
        instance.word = validated_data.get('word', instance.word)
        instance.save()
        return instance
'''