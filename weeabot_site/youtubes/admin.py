# vim: set ts=2 expandtab:
from django.contrib import admin
from models import Youtube
from models import Tag

class TagInline(admin.TabularInline):
  model = Youtube.tags.through

class YoutubeAdmin(admin.ModelAdmin):
  inlines = [
    TagInline,
  ]
  exclude = ['filehash', 'tags']

class TagAdmin(admin.ModelAdmin):
  list_display = ('name')

admin.site.register(Youtube, YoutubeAdmin)
admin.site.register(Tag)
