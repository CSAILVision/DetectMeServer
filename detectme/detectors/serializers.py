from rest_framework import serializers
from .models import Detector


class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('id', 'name', 'target_class',
                  'author', 'is_public', 'average_image',
                  'created_at', 'updated_at',
                  'weights', 'sizes', 'support_vectors')
        read_only = ('author')
        
