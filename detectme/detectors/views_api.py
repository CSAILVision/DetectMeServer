from rest_framework import generics, permissions
from .models import Detector, Rating, AnnotatedImage
from .serializers import DetectorSerializer, AnnotatedImageSerializer,\
                          RatingSerializer, SupportVectorSerializer
from .views import get_allowed_detectors
# from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DetectorAPIList(generics.ListCreateAPIView):
    serializer_class = DetectorSerializer

    # def get_serializer(self, instance=None, data=None, files=None, many=False, partial=False):
    #     print 'getting serializer!!'
    #     if not files:
    #         files = {'average_image':''}
    #     print files
    #     return super(DetectorAPIList, self).get_serializer(instance, data, files, many, partial)


    def pre_save(self, obj):
        obj.author = self.request.user.get_profile()
        print 'pre save is being called!!'

    def get_queryset(self):
        return (Detector.objects
                .filter(get_allowed_detectors(self.request.user))
                .order_by('-created_at'))


class DetectorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetectorSerializer
    model = Detector
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
                          # IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        # remove all the images and wait for the new ones to be updated
        obj.annotatedimage_set.all().delete()
        obj.author = self.request.user.get_profile()

    def get_queryset(self):
        qs = super(DetectorAPIDetail, self).get_queryset()
        return qs.filter(get_allowed_detectors(self.request.user))


class AnnotatedImageAPIList(generics.ListCreateAPIView):
    serializer_class = AnnotatedImageSerializer

    def pre_save(self, obj):
        obj.author = self.request.user.get_profile()


class AnnotatedImageAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnnotatedImageSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          # IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user.get_profile()


class AnnotatedImagesForDetector(generics.ListAPIView):
    serializer_class = AnnotatedImageSerializer

    def get_queryset(self):
        # Returns list of AnnotatedImage for the requested detector
        detector = self.kwargs['detector']
        return AnnotatedImage.objects.filter(detector=detector)


class SupportVectorsForDetector(generics.RetrieveAPIView):
    serializer_class = SupportVectorSerializer
    model = Detector


class RatingAPIList(APIView):
    """
    Store the rating as a new rating only if it is the first
    time this user rates this detector
    """

    def post(self, request, format=None):
        serializer = RatingSerializer(data=request.DATA)
        author = self.request.user.get_profile()

        if serializer.is_valid():

            try:
                previous_rating = Rating.objects.get(author=author,
                                                     detector=serializer.object.detector)
                previous_rating.rating = serializer.object.rating
                previous_rating.save()
            
            except Rating.DoesNotExist:
                serializer.object.author = author
                serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

