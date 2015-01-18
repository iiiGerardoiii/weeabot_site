from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jisho.models import Definition
from jisho.serializers import DefinitionSerializer

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