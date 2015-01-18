from django.conf.urls import url
from jisho import views

urlpatterns = [
    url(r'^jisho/$', views.definition_list),
    url(r'^jisho/(?P<pk>[0-9]+)/$', views.definition_detail),
]