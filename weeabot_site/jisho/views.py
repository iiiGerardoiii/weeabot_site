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

class JSONResponse(HttpResponse):
  """
  An HttpResponse that renders its content into JSON.
  """
  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def definition_list(request):
  """
  List all dictonary entries, or create a new one.
  """
  if request.method == 'GET':
    definitions = Definition.objects.all()
    serializer = DefinitionSerializer(definitions, many=True)
    return JSONResponse(serializer.data)

  elif request.method == 'POST':
    print 'post request'
    data = JSONParser().parse(request)
    print str(data)
    serializer = DefinitionSerializer(data=data)
    if serializer.is_valid():
      print 'VALID'
      serializer.save()
      return JSONResponse(serializer.data, status=201)
    else:
      print 'NOT VALID'
    return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def definition_detail(request, pk):
  """
  Retrieve, update or delete a definition.
  """
  try:
    single_definition = Definition.objects.get(pk=pk)
  except Definition.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = DefinitionSerializer(single_definition)
    return JSONResponse(serializer.data)

  elif request.method == 'PUT':
    print 'definition_detail PUT'
    data = JSONParser().parse(request)
    serializer = DefinitionSerializer(single_definition, data=data)
    if serializer.is_valid():
      print 'serializer VALID'
      serializer.save()
      return JSONResponse(serializer.data)
    else:
      print 'serializer not valid'
    return JSONResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    single_definition.delete()
    return HttpResponse(status=204)