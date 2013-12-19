from rest_framework import serializers
from .models import Detector, AnnotatedImage, Rating


class DetectorSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(required=False,
                                                source='parent')
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    average_rating = serializers.Field()
    number_ratings = serializers.Field()

    class Meta:
        model = Detector
        fields = ('id', 'name', 'target_class',
                  'author', 'is_public', 'average_image',
                  'uploaded_at', 'is_deleted', 'average_rating',
                  'weights', 'sizes', 'parent', 'support_vectors',
                  'training_log', 'created_at', 'updated_at', 'number_ratings')
        read_only = ('author', 'uploaded_at', 'id', 'average_rating',
                     'number_ratings')

    def to_native(self, obj):
        '''Support vectors field write only'''
        ret = super(DetectorSerializer, self).to_native(obj)
        del ret['support_vectors']
        return ret


class AnnotatedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotatedImage
        fields = ('id', 'image_jpeg',
                  'image_height', 'image_width',
                  'box_x', 'box_y',
                  'box_width', 'box_height',
                  'location_latitude', 'location_longitude',
                  'motion_quaternionX', 'motion_quaternionY',
                  'motion_quaternionZ', 'motion_quaternionW',
                  'detector')
        read_only = ('uploaded_at', 'image_height', 'image_width')


class SupportVectorSerializer(serializers.ModelSerializer):
    ''' Class to just return the SV associated to a detector'''
    class Meta:
        model = Detector
        fields = ('support_vectors',)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('detector', 'rating')
