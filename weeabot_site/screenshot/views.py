from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from screenshot.models import Screenshot
from screenshot.serializers import ScreenshotSerializer
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

from screenshot import tasks
import urllib
import json

from django.conf import settings

def in_group(user, groupname):
  return u.groups.filter(name=groupname).count() == 0


def home(request):
  #handling post dropdown result
  images = Screenshot.objects.all().order_by('timestamp').reverse()
  #first_date = definitions[len(definitions)-1].timestamp
  #last_date = definitions[0].timestamp
  #lists = VocabularyList.objects.all()
  paginator = Paginator(images, 3) # Show 3 thumbnails per page
  page = request.GET.get('page')
  try:
    images = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    images = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    images = paginator.page(paginator.num_pages)

  t = loader.get_template('screenshot/index.html')
  c = RequestContext(request, {
    'title' : 'Weeabot Stream Screenshots',
    'description' : 'Recent Stream Screenshots',
    #'first_date' : first_date,
    #'last_date' : last_date,
    'images': images,
    'paginator' : paginator,
    #'lists' : lists,
    'editable' : False, #request.user.is_staff,
    'deleteable' : False,
    'show_vocab_lists' : False,
    'image_dir' : settings.SCREENSHOT_DOWNLOAD_DIR,
    })
  return HttpResponse(t.render(c))


'''
RESTful interface support
'''

class ScreenshotList(ListAPIView):
  '''
  List all screenshot or create a new entry
  '''
  queryset = Screenshot.objects.all()
  serializer_class = ScreenshotSerializer
  paginate_by = 10

class ScreenshotDetail(RetrieveAPIView):
  '''
  Show a single webm database entry
  '''
  queryset = Screenshot.objects.all()
  serializer_class = ScreenshotSerializer


class NewScreenshot(APIView):
  '''Initiate an async screenshot .
  '''
  #need to tie to a model to support permissions
  queryset = Screenshot.objects.all()

  def post(self, request, *args, **kwargs):
    print "POST HANDLER" 
    nick = request.DATA.get('nick', None)
    url = request.DATA.get('url', None)
    channel = request.DATA.get('channel', None)
    #already an entry with this URL?
    #if Screenshot.objects.filter(url=url).count():
    #  return Response({"success": False})
    if nick and url and channel:
      print "going to start task for url: " + url
      tasks.take_screenshot.delay(nick, channel, url, settings.SCREENSHOT_DOWNLOAD_DIR)
      return Response({"success": True})
    else:
      return Response({"success": False})
