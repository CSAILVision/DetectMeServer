from rest_framework import generics
from rest_framework.parsers import JSONParser
from .serializers import PerformanceSerializer
from .models import Category


class PerformanceAPICreate(generics.CreateAPIView):
    serializer_class = PerformanceSerializer
    parser_classes = (JSONParser,)
