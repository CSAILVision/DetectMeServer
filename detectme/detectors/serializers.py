from rest_framework import serializers
from .models import Detector

class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detector
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')