# vim: set ts=2 expandtab:
from django.contrib import admin
from models import Definition
#from models import VocabularyList

#class DefinitionInline(admin.TabularInline):
#  model = VocabularyList.entries.through

#class VocabularyListAdmin(admin.ModelAdmin):
#  inlines = [DefinitionInline,]


class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'channel', 'nick', 'word', 'text', 'url')

admin.site.register(Definition, DefinitionAdmin)
#admin.site.register(VocabularyList, VocabularyListAdmin)
