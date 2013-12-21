from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import DetectMeProfile
from .serializers import UserSerializer, DetectMeProfileSerializer


class AccountAPICreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post_save(self, obj, created=False):
        if(created):
            p = DetectMeProfile(user=obj, favourite_snack='tbd')
            p.save()


class AccountAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetectMeProfileSerializer
    model = DetectMeProfile

    def get_queryset(self):
        return DetectMeProfile.objects.all()

    def get_object(self):
        # used to be able to update the profil picture
        # just with the username
        queryset = self.get_queryset()
        filter = {}
        filter['user__username'] = self.kwargs['username']
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def post_save(self, obj, created=False):
        if created:
            serializer = DetectMeProfileSerializer(data=request.DATA)
            obj.mugshot = serializer.mugshot
            obj.save()
