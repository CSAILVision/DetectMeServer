from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from .serializers import PerformanceSerializer


class PerformanceAPICreate(generics.CreateAPIView):
    serializer_class = PerformanceSerializer
    parser_classes = (JSONParser,)
    permission_classes = (IsAdminUser,)
