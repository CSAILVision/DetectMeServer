from rest_framework import generics
from .models import DetectMeProfile
from .serializers import UserSerializer


class AccountAPICreate(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post_save(self, obj, created=False):
        if(created):
            p = DetectMeProfile(user=obj, favourite_snack='tbd')
            p.save()




# curl -i -X POST http://128.30.99.161:8000/accouns/api/create -d "code=print 123"