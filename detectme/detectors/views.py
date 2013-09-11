from .models import Detector
from .serializers import DetectorSerializer
from rest_framework import generics


# API Views

class DetectorList(generics.ListCreateAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorSerializer


class DetectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorSerializer
