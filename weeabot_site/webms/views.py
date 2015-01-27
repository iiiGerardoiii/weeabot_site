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
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from webms import tasks
import urllib
import json

from django.conf import settings

def in_group(user, groupname):
  return u.groups.filter(name=groupname).count() == 0

'''
RESTful interface support
'''

class WebmList(ListAPIView):
  '''
  List all webms or create a new entry
  '''
  queryset = Webm.objects.all()
  serializer_class = WebmSerializer
  paginate_by = 10

class WebmDetail(RetrieveAPIView):
  '''
  Show a single webm database entry
  '''
  queryset = Webm.objects.all()
  serializer_class = WebmSerializer


class NewWebmView(APIView):
  '''Add a new webm. Kick off processes.
  '''
  #need to tie to a model to support permissions
  queryset = Webm.objects.all()

  def post(self, request, *args, **kwargs):
    nick = request.DATA.get('nick', None)
    url = request.DATA.get('url', None)
    channel = request.DATA.get('channel', None)
    #already an entry with this URL?
    if Webm.objects.filter(url=url).count():
      return Response({"success": False})
    if nick and url and channel:
      tasks.new_webm.delay(nick, channel, url, settings.WEBMS_DOWNLOAD_DIR)
      return Response({"success": True})
    else:
      return Response({"success": False})