from rest_framework import serializers
from .models import Detector


class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('id', 'name', 'object_class',
                  'created_by', 'public', 'average_image', 'hash_value')
        exclude = ('created_by',)
