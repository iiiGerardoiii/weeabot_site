from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from webms.models import Webm
from webms.serializers import WebmSerializer
from django.template import Context, RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import sys, traceback

from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView

from webms import tasks


def in_group(user, groupname):
  return u.groups.filter(name=groupname).count() == 0

'''
RESTful interface support
'''

class WebmList(ListCreateAPIView):
  '''
  List all webms or create a new entry
  '''
  queryset = Webm.objects.all()
  serializer_class = WebmSerializer
  paginate_by = 10

  #def post(self, request, *args, **kwargs):
  #  #initiate a download asynchronously
  #  tasks.download.delay('http://i.4cdn.org/pol/1421793863465.jpg','', 'xxx.jpg')
  #  return self.create(request, *args, **kwargs)

class WebmDetail(RetrieveAPIView):
  '''
  Show a single webm database entry
  '''
  queryset = Webm.objects.all()
  serializer_class = WebmSerializer
