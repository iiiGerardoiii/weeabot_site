# vim: set ts=2 expandtab:
from django.contrib import admin
from models import Webm
#from models import VocabularyList

#class DefinitionInline(admin.TabularInline):
#  model = VocabularyList.entries.through

#class VocabularyListAdmin(admin.ModelAdmin):
#  inlines = [DefinitionInline,]


class WebmAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'channel', 'nick', 'filename', 'filehash')

admin.site.register(Webm, WebmAdmin)
#admin.site.register(VocabularyList, VocabularyListAdmin)
