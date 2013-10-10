from rest_framework import generics
from .models import DetectMeProfile
from .serializers import UserSerializer


class AccountAPICreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post_save(self, obj, created=False):
        if(created):
            p = DetectMeProfile(user=obj, favourite_snack='tbd')
            p.save()
