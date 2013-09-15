from django.views.generic import ListView, DetailView
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FileUploadParser
from .models import Detector
from .serializers import DetectorSerializer
from .permissions import IsOwnerOrReadOnly


# API Views
class DetectorAPIList(generics.ListCreateAPIView):
    serializer_class = DetectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser, FileUploadParser,)

    def pre_save(self, obj):
        obj.created_by = self.request.user.get_profile()

    def get_queryset(self):
        return (Detector.objects
                .filter(get_allowed_detectors(self.request.user))
                .order_by('-created_at'))


class DetectorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    parser_classes = (MultiPartParser, FileUploadParser,)
    model = Detector

    def pre_save(self, obj):
        obj.created_by = self.request.user.get_profile()

    def get_queryset(self):
        qs = super(DetectorAPIDetail, self).get_queryset()
        return qs.filter(get_allowed_detectors(self.request.user))


# General views
class DetectorList(ListView):
    model = Detector
    context_object_name = 'detector_list'
    template_name = 'detectors/detector_list'

    def get_queryset(self):
        return (Detector.objects
                .filter(get_allowed_detectors(self.request.user))
                .order_by('-created_at'))


class DetectorDetail(DetailView):
    model = Detector
    template_name = 'detectors/detector_detail'

    def get_queryset(self):
        qs = super(DetectorDetail, self).get_queryset()
        return qs.filter(get_allowed_detectors(self.request.user))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetectorDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['annotations_list'] = self.object.annotations.all()
        return context


def get_allowed_detectors(user):
    if user.is_authenticated():
        return (Q(created_by=user.get_profile()) | Q(public=True))
    else:
        return Q(public=True)
