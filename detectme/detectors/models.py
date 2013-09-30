from django.conf import settings
from django.db import models
from PIL import Image
from datetime import datetime
import uuid


class Detector(models.Model):
    name = models.CharField(max_length=50)
    target_class = models.CharField(max_length=50)
    author = models.ForeignKey('accounts.LabelMeProfile', editable=False)
    is_public = models.BooleanField(default=False)
    average_image = models.ImageField(upload_to='average_image/',
                                      default='average_image/default.jpg')
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    weights = models.TextField()  # arrays to be serialized with JSON
    sizes = models.TextField()
    support_vectors = models.TextField()
    hash_value = models.CharField(max_length=32, blank=True,
                                  editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.hash_value:
            self.hash_value = uuid.uuid1().hex
        if not self.created_at:
            self.created_at = datetime.now()
        super(Detector, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s: %s class by %s' % (self.name, self.target_class,
                                        self.author.user)

    class Meta:
        ordering = ('created_at',)


class AnnotatedImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image_jpeg = models.ImageField(upload_to=settings.MEDIA_ROOT)
    image_height = models.PositiveSmallIntegerField(editable=False, blank=True)
    image_width = models.PositiveSmallIntegerField(editable=False, blank=True)
    box_x = models.PositiveSmallIntegerField(editable=False, blank=True)
    box_y = models.PositiveSmallIntegerField(editable=False, blank=True)
    box_height = models.PositiveSmallIntegerField(editable=False, blank=True)
    box_width = models.PositiveSmallIntegerField(editable=False, blank=True)
    author = models.ForeignKey('accounts.LabelMeProfile', editable=False)
    detector = models.ForeignKey(Detector)

    def save(self, *args, **kwargs):
        im = Image.open(self.image_.path)
        self.image_width = im.size[0]
        self.image_height = im.size[1]
        super(AnnotatedImage, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.image_jpeg.name
