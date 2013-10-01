from rest_framework import serializers
from .models import Detector, AnnotatedImage


class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('id', 'name', 'target_class',
                  'author', 'is_public', 'average_image',
                  'uploaded_at',  # created_at, updated_at
                  'weights', 'sizes', 'support_vectors')
        read_only = ('author', 'uploaded_at', 'id')


class AnnotatedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotatedImage
        fields = ('id', 'image_jpeg',
                  'image_height', 'image_width',
                  'box_x', 'box_y',
                  'box_width', 'box_height',
                  'author', 'detector')
        read_only = ('author', 'uploaded_at', 'image_height', 'image_width')
