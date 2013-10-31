from django.contrib.auth.models import User
from .models import DetectMeProfile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class DetectMeProfileSerializer(serializers.ModelSerializer):
    mugshot = serializers.ImageField()

    class Meta:
        model = DetectMeProfile
        fields = ('mugshot', )

