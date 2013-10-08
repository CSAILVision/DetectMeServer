from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DetectMeProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class DetectMeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = DetectMeProfile
