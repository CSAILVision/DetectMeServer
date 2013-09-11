from django.views.generic import ListView, DetailView
from rest_framework import generics
from .models import Detector
from .serializers import DetectorSerializer


# API Views
class DetectorAPIList(generics.ListCreateAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorSerializer


class DetectorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detector.objects.all()
    serializer_class = DetectorSerializer


# General views
class DetectorList(ListView):
    model = Detector
    context_object_name = 'detector_list'


class DetectorDetail(DetailView):
    model = Detector
    template_name = 'detectors/detector_detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetectorDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['annotations_list'] = self.object.annotations.all()
        return context
