from django.conf.urls import url
from webms import views

from django.conf.urls import include

urlpatterns = [
  url(r'^$', 'webms.views.home', name='home'),
  #url(r'^vocab/$', 'jisho.views.VocabularyListsView', name='VocabularyListsView'),
  #url(r'^vocab/(?P<listname>\w+)', 'jisho.views.VocabularyListsView', name='VocabularyListView'),
  #url(r'^nick/(?P<nick>\w+)', 'jisho.views.NickView', name='NickView'),
  url(r'^api/$', views.WebmList.as_view(),name='Webm-list'),
  url(r'^api/(?P<pk>[0-9]+)/$', views.WebmDetail.as_view(),name='Webm-detail'),
  url(r'^new/$', views.NewWebmView.as_view(), name='Add-Webm'),
]
