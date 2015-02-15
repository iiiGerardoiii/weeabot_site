from django.conf.urls import url
from youtubes import views

from django.conf.urls import include

urlpatterns = [
  url(r'^$', 'youtubes.views.home', name='home'),
  #url(r'^vocab/$', 'jisho.views.VocabularyListsView', name='VocabularyListsView'),
  #url(r'^vocab/(?P<listname>\w+)', 'jisho.views.VocabularyListsView', name='VocabularyListView'),
  #url(r'^nick/(?P<nick>\w+)', 'jisho.views.NickView', name='NickView'),
  url(r'^api/$', views.YoutubeList.as_view(),name='Youtube-list'),
  url(r'^api/(?P<pk>[0-9]+)/$', views.YoutubeDetail.as_view(),name='Youtube-detail'),
  url(r'^new/$', views.NewYoutubeView.as_view(), name='Add-Youtube'),
]
