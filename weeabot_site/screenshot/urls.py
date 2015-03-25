from django.conf.urls import url
from screenshot import views

from django.conf.urls import include

urlpatterns = [
  url(r'^$', 'screenshot.views.home', name='home'),
  #url(r'^vocab/$', 'jisho.views.VocabularyListsView', name='VocabularyListsView'),
  #url(r'^vocab/(?P<listname>\w+)', 'jisho.views.VocabularyListsView', name='VocabularyListView'),
  #url(r'^nick/(?P<nick>\w+)', 'jisho.views.NickView', name='NickView'),
  url(r'^api/$', views.ScreenshotList.as_view(),name='Screenshot-list'),
  url(r'^api/(?P<pk>[0-9]+)/$', views.ScreenshotDetail.as_view(),name='Screenshot-detail'),
  url(r'^new/$', views.NewScreenshot.as_view(), name='Add-Screenshot'),
]
