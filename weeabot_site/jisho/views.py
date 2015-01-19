from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jisho.models import Definition
from jisho.serializers import DefinitionSerializer
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


def in_group(user, groupname):
  return u.groups.filter(name=groupname).count() == 0

def home(request):
  #handling post dropdown result
  '''
  if request.method == 'POST':
    list_name = request.POST.get('vlist', '')
    if list_name == '...':
      return HttpResponseRedirect('')
    definition_pk = request.POST.get('definition', '')
    definition = Definition.objects.get(pk=definition_pk)
    new_list = VocabularyList.objects.get(name=list_name)
    definition.lists.add(new_list)
    return HttpResponseRedirect('')
  '''
  definitions = Definition.objects.all().order_by('timestamp').reverse()
  #first_date = definitions[len(definitions)-1].timestamp
  #last_date = definitions[0].timestamp
  #lists = VocabularyList.objects.all()
  paginator = Paginator(definitions, 30) # Show 30 contacts per page
  page = request.GET.get('page')
  try:
    definitions = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    definitions = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    definitions = paginator.page(paginator.num_pages)

  t = loader.get_template('jisho/index.html')
  c = RequestContext(request, {
    'title' : 'Weeabot Jisho Lookups',
    'description' : 'Recent weeabot irc bot .jisho lookups',
    #'first_date' : first_date,
    #'last_date' : last_date,
    'definitions': definitions,
    'paginator' : paginator,
    #'lists' : lists,
    'editable' : False, #request.user.is_staff,
    'deleteable' : False,
    'show_vocab_lists' : False,
    })
  return HttpResponse(t.render(c))


'''
RESTful interface support
'''
'''
class JSONResponse(HttpResponse):
  """
  An HttpResponse that renders its content into JSON.
  """
  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)
'''
class DefinitionList(ListCreateAPIView):
  '''
  List all definitions, or create a new definition.
  '''
  queryset = Definition.objects.all()
  serializer_class = DefinitionSerializer
  paginate_by = 10

class DefinitionDetail(RetrieveAPIView):
  '''
  Show an individual definition by id
  '''
  queryset = Definition.objects.all()
  serializer_class = DefinitionSerializer
