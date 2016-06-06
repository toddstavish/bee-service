from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from compare_polygons.models import Footprint
from compare_polygons.serializers import FootprintSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def compare_polys_polis(request, format=None):
    print('am i here')
    content = {'user_count': 1}
    return Response(content)

    #data = JSONParser().parse(request)
    #serializer = FootprintSerializer(data=data)
    #if serializer.is_valid():
        #return JSONResponse(serializer.data, status=201)
    #return JSONResponse(serializer.errors, status=400)
