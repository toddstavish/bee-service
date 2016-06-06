from rest_framework import serializers
from compare_polygons.models import Footprint


class FootprintSerializer(serializers.Serializer):
    fp = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Footprint.objects.create(**validated_data)
