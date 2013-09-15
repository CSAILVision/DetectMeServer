from django.conf import settings
from django.db import models
from django.db.models.signals import m2m_changed
from PIL import Image
from datetime import datetime
import uuid


class Detector(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    object_class = models.CharField(max_length=50, editable=False, blank=True)
    average_image = models.ImageField(upload_to='average_image/',
                                      default='average_image/default.jpg')
    support_vectors = models.TextField()  # arrays to be serialized with JSON
    weights = models.TextField()
    dimensions = models.TextField()
    created_by = models.ForeignKey('accounts.LabelMeProfile', editable=False)
    annotations = models.ManyToManyField('Annotation', blank=True, null=True)
    public = models.BooleanField(default=False)
    hash_value = models.CharField(max_length=32, blank=True,
                                  editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.hash_value:
            self.hash_value = uuid.uuid1().hex
        if not self.created_at:
            self.created_at = datetime.now()
        super(Detector, self).save(*args, **kwargs)

    # Handler for updating the detector class when annotations are stored
    @staticmethod
    def update_detector_class(sender, instance, action,
                              reverse, model, pk_set, **kwargs):
        if action == 'post_add' and not instance.object_class:
            if instance.annotations.all():
                instance.object_class = instance.annotations.all()[0].object_class
                instance.save()

    def __unicode__(self):
        return u'%s: %s class by %s' % (self.name, self.object_class,
                                        self.created_by.user)

    class Meta:
        ordering = ('created_at',)


# register the signal
m2m_changed.connect(Detector.update_detector_class,
                    sender=Detector.annotations.through)


class Annotation(models.Model):
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    object_class = models.CharField(max_length=50)
    position = models.TextField()
    image = models.ForeignKey('AnnotatedImage')

    def __unicode__(self):
        return u'Annotation for %s' % self.object_class


class AnnotatedImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    height = models.PositiveSmallIntegerField(editable=False, blank=True)
    width = models.PositiveSmallIntegerField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        im = Image.open(self.image.path)
        self.width = im.size[0]
        self.height = im.size[1]
        super(AnnotatedImage, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.image.name


class Performance(models.Model):
    detector = models.OneToOneField('Detector')
    auc = models.FloatField()
    fps = models.FloatField()
    time_learning = models.FloatField()

    def __unicode__(self):
        return u'%s' % self.auc
