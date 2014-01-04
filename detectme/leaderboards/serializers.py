from rest_framework import serializers
from .models import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ('detector', 'average_precision', 'precision',
                  'recall', 'test_set')
