from django.shortcuts import render
from django.db.models import F

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


def home(request):
  #handling post dropdown result
  images = Webm.objects.all()
  #first_date = definitions[len(definitions)-1].timestamp
  #last_date = definitions[0].timestamp
  #lists = VocabularyList.objects.all()
  paginator = Paginator(images, 70) # Show 70 thumbnails per page
  page = request.GET.get('page')
  try:
    images = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    images = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    images = paginator.page(paginator.num_pages)

  t = loader.get_template('webms/index.html')
  c = RequestContext(request, {
    'title' : 'Weeabot Image Scrapes',
    'description' : 'Recent IRC scraped images.',
    #'first_date' : first_date,
    #'last_date' : last_date,
    'images': images,
    'paginator' : paginator,
    #'lists' : lists,
    'editable' : False, #request.user.is_staff,
    'deleteable' : False,
    'show_vocab_lists' : False,
    'image_dir' : settings.WEBMS_DOWNLOAD_DIR,
    })
  return HttpResponse(t.render(c))


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
      w = Webm.objects.get(url=url)
      w.hits = w.hits + 1
      w.save()
      return Response({"success": True})
    if nick and url and channel:
      tasks.new_webm.delay(nick, channel, url, settings.WEBMS_DOWNLOAD_DIR)
      return Response({"success": True})
    else:
      return Response({"success": False})
