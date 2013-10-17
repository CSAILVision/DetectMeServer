from rest_framework import serializers
from .models import Detector, AnnotatedImage


class DetectorSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(required=False,
                                                source='parent')
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')

    class Meta:
        model = Detector
        fields = ('id', 'name', 'target_class',
                  'author', 'is_public', 'average_image',
                  'uploaded_at', 'is_deleted',
                  'weights', 'sizes', 'support_vectors', 'parent')
        read_only = ('author', 'uploaded_at', 'id')


class AnnotatedImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnnotatedImage
        fields = ('id', 'image_jpeg',
                  'image_height', 'image_width',
                  'box_x', 'box_y',
                  'box_width', 'box_height',
                  'detector')
        read_only = ('uploaded_at', 'image_height', 'image_width')


# http://stackoverflow.com/questions/2929422/multi-thread-conversation-in-django-like-reddit
