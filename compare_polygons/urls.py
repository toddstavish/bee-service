from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from compare_polygons import views

urlpatterns = [
    url(r'^polis/$', views.compare_polys_polis),
    url(r'^jaccard/$', views.compare_polys_jaccard)
]

urlpatterns = format_suffix_patterns(urlpatterns)
