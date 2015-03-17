from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

'''
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
'''

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='weeabot_site/index.html'),
      name='home'),
    url(r'^jisho/', include('jisho.urls')),
    url(r'^webms/', include('webms.urls')),
    url(r'^youtubes/', include('youtubes.urls')),
    url(r'^screenshot/', include('screenshot.urls')),
    #url(r'^$', 'weeabot_site.views.home', name='home'),
    #url(r'^jisho/', include('jisho.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
