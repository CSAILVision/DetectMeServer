from django.db.models import Q
from rest_framework import generics, permissions
# from rest_framework.parsers import MultiPartParser, FileUploadParser, JSONParser
from .models import Detector, Rating
from .serializers import DetectorSerializer, AnnotatedImageSerializer, RatingSerializer
# from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DetectorAPIList(generics.ListCreateAPIView):
    serializer_class = DetectorSerializer

    def pre_save(self, obj):
        obj.author = self.request.user.get_profile()

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


def get_allowed_detectors(user):
    if user.is_authenticated():
        return (Q(author=user.get_profile()) | Q(is_public=True))
    else:
        return Q(is_public=True)


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


# class RatingAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = RatingSerializer

#     def pre_save(self, obj):
#         obj.author = self.request.user.get_profile()

