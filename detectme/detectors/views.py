from django.views.generic import ListView, DetailView
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FileUploadParser, JSONParser
from .models import Detector, AnnotatedImage
from .serializers import DetectorSerializer, AnnotatedImageSerializer
from .permissions import IsOwnerOrReadOnly


# API Views
class DetectorAPIList(generics.ListCreateAPIView):
    serializer_class = DetectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FileUploadParser,)

    def pre_save(self, obj):
        obj.author = self.request.user.get_profile()
        #print 'saving author with:' + self.request.user.get_profile()

    def get_queryset(self):
        return (Detector.objects
                .filter(get_allowed_detectors(self.request.user))
                .order_by('-created_at'))


class DetectorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetectorSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
                          #IsOwnerOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FileUploadParser,)
    model = Detector

    def pre_save(self, obj):
        # remove all the images and wait for the new ones to be updated
        obj.annotatedimage_set.all().delete()
        #obj.author = self.request.user.get_profile()

    def get_queryset(self):
        qs = super(DetectorAPIDetail, self).get_queryset()
        return qs.filter(get_allowed_detectors(self.request.user))


class AnnotatedImageAPIList(generics.ListCreateAPIView):
    serializer_class = AnnotatedImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FileUploadParser,)
    model = AnnotatedImage

    def pre_save(self, obj):
        obj.author = self.request.user.get_profile()
        #print 'saving author with:' + self.request.user.get_profile()


class AnnotatedImageAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnnotatedImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FileUploadParser,)
    model = AnnotatedImage

    def pre_save(self, obj):
        obj.author = self.request.user.get_profile()


###### General views
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
        context['annotatedimage_list'] = self.object.annotatedimage_set.all()
        return context


def get_allowed_detectors(user):
    if user.is_authenticated():
        return (Q(author=user.get_profile()) | Q(is_public=True))
    else:
        return Q(is_public=True)
