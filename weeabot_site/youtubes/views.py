from django.shortcuts import render
from django.db.models import F

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from youtubes.models import Youtube
from youtubes.serializers import YoutubeSerializer
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
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView

from youtubes import tasks
import urllib
import json

from django.conf import settings

def in_group(user, groupname):
  return u.groups.filter(name=groupname).count() == 0


def home(request):
  #handling post dropdown result
  y = Youtube.objects.all()
  #first_date = definitions[len(definitions)-1].timestamp
  #last_date = definitions[0].timestamp
  #lists = VocabularyList.objects.all()
  paginator = Paginator(y, 70) # Show 70 thumbnails per page
  page = request.GET.get('page')
  try:
    y = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    y = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    y = paginator.page(paginator.num_pages)

  t = loader.get_template('youtubes/index.html')
  c = RequestContext(request, {
    'title' : 'Weeabot Youtube Scrapes',
    'description' : 'Recently scraped youtube links.',
    #'first_date' : first_date,
    #'last_date' : last_date,
    'youtubes': y,
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

class YoutubeList(ListCreateAPIView):
  '''
  List all youtubes or create a new entry
  '''
  queryset = Youtube.objects.all()
  serializer_class = YoutubeSerializer
  paginate_by = 10

class YoutubeDetail(RetrieveAPIView):
  '''
  Show a single webm database entry
  '''
  queryset = Youtube.objects.all()
  serializer_class = YoutubeSerializer


class NewYoutubeView(APIView):
  queryset = Youtube.objects.all()
  serializer_class = YoutubeSerializer
#  '''Add a new webm. Kick off processes.
#  '''
#  #need to tie to a model to support permissions
#  queryset = Youtube.objects.all()
#
#  def post(self, request, *args, **kwargs):
#    nick = request.DATA.get('nick', None)
#    url = request.DATA.get('url', None)
#    channel = request.DATA.get('channel', None)
#    #already an entry with this URL?
#    if Youtube.objects.filter(url=url).count():
#      w = Youtube.objects.get(url=url)
#      w.hits = w.hits + 1
#      w.save()
#      return Response({"success": True})
#    else:
#      y = Youtube()
#    if nick and url and channel:
#      tasks.new_webm.delay(nick, channel, url, settings.WEBMS_DOWNLOAD_DIR)
#      return Response({"success": True})
#    else:
#      return Response({"success": False})
