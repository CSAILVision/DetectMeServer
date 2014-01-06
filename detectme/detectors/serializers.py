from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Detector, AnnotatedImage, Rating, ExtraInfo



class DetectorSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(required=False,
                                                source='parent')
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    average_rating = serializers.Field()
    number_ratings = serializers.Field()
    number_images = serializers.Field()

    support_vectors = serializers.Field()
    training_log = serializers.Field()


    class Meta:
        model = Detector
        fields = ('id', 'name', 'target_class',
                  'author', 'is_public', 'average_image',
                  'uploaded_at', 'is_deleted', 'average_rating',
                  'weights', 'sizes', 'parent', 'created_at',
                  'updated_at', 'number_ratings', 'number_images')
        read_only = ('author', 'uploaded_at', 'id', 'average_rating',
                     'number_ratings', 'number_images')

    def from_native(self, data, files):
        """
        Override the default method to extract extra information and store it
        separetedly
        """
        sv = data.get('support_vectors')
        tl = data.get('training_log')
        detector = super(serializers.ModelSerializer, self).from_native(data, files)
        extra_info = ExtraInfo(detector=detector, support_vectors=sv, training_log=tl)
        if not self._errors:
            return self.full_clean(detector)


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
    """
    Just returns the support vectors for the detector retraining
    """
    support_vectors = serializers.Field()

    class Meta:
        model = Detector
        fields = ('support_vectors', )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('detector', 'rating')


# class PerformanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Performance
#         fields = ('detector', 'average_precision', 'precision',
#                   'recall', 'test_set')

