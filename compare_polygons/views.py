import numpy as np
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon
from compare_polygons import polis as pls
from compare_polygons import jaccard as jcd

# Create your views here.

@csrf_exempt
@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def compare_polys_polis(request, format=None):
    poly_1, poly_2 = create_polys(request)
    polis = pls.compare_polys(poly_1, poly_2)
    content = {'polis': polis}
    return Response(content)


@csrf_exempt
@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def compare_polys_jaccard(request, format=None):
    poly_1, poly_2 = create_polys(request)
    jaccard = jcd.compare_polys(poly_1, poly_2)
    content = {'jaccard': jaccard}
    return Response(content)


def create_polys(request):
    params = request.query_params.iteritems()
    polys={}
    for k,v in params:
        coords = np.array([float(f) for f in v.split(',')])
        polys[k] = np.reshape(coords, (-1, 2))
    return (Polygon(polys.values()[0]), Polygon(polys.values()[1]))
