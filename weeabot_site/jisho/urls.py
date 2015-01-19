from django.conf.urls import url
from jisho import views

from django.conf.urls import include

urlpatterns = [
  url(r'^$', 'jisho.views.home', name='home'),
  #url(r'^vocab/$', 'jisho.views.VocabularyListsView', name='VocabularyListsView'),
  #url(r'^vocab/(?P<listname>\w+)', 'jisho.views.VocabularyListsView', name='VocabularyListView'),
  #url(r'^nick/(?P<nick>\w+)', 'jisho.views.NickView', name='NickView'),
  url(r'^api/$', views.DefinitionList.as_view()),
  #url(r'^entry/(?P<pk>[0-9]+)/$', views.definition_detail),
]
