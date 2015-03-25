# vim: set ts=2 expandtab:
from django.contrib import admin
from models import Screenshot

#class TagInline(admin.TabularInline):
#  model = Webm.tags.through

class ScreenshotAdmin(admin.ModelAdmin):
  pass

admin.site.register(Screenshot, ScreenshotAdmin)
