from django.db import models

# Create your models here.


class Detector(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_add=True)
    name = models.CharField()
    object_class = models.CharField()
    average_image = models.ImageField()
    time_learning = models.FloatField()
    support_vectors = models.TextField()  # arrays to be serialized with JSON
    weights = models.TextField()
    dimensions = models.TextField()


class Annotation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_add=True)
    object_class = models.CharField()
    position = models.TextField()


class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    dimensions = models.TextField()
