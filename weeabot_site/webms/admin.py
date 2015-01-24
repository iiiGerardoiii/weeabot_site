# vim: set ts=2 expandtab:
from django.contrib import admin
from models import Webm
from models import Tag

class TagInline(admin.TabularInline):
  model = Webm.tags.through

class WebmAdmin(admin.ModelAdmin):
  inlines = [
    TagInline,
  ]
  exclude = ['filehash', 'tags']

class TagAdmin(admin.ModelAdmin):
  list_display = ('name')

admin.site.register(Webm, WebmAdmin)
admin.site.register(Tag)
