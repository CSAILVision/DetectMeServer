from django.conf import settings
from django.db import models
from PIL import Image
from django.db.models.signals import m2m_changed

# Create your models here.


class Detector(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    name = models.CharField(max_length=50)
    object_class = models.CharField(max_length=50, editable=False, blank=True)
    average_image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    time_learning = models.FloatField()
    support_vectors = models.TextField()  # arrays to be serialized with JSON
    weights = models.TextField()
    dimensions = models.TextField()
    user = models.ForeignKey('accounts.LabelMeProfile', editable=False)
    annotations = models.ManyToManyField('Annotation')

    def save(self, *args, **kwargs):
        super(Detector, self).save(*args, **kwargs)

    # Handler for updating the detector class when annotations are stored
    @staticmethod
    def update_detector_class(sender, instance, action, reverse, model, pk_set, **kwargs):
        if action == 'post_add' and not instance.object_class:
            instance.object_class = instance.annotations.all()[0].object_class
            instance.save()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.object_class)

    class Meta:
        ordering = ('created',)


# register the signal
m2m_changed.connect(Detector.update_detector_class, sender=Detector.annotations.through)


class Annotation(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    object_class = models.CharField(max_length=50)
    position = models.TextField()
    image = models.ForeignKey('AnnotatedImage')

    def __unicode__(self):
        return u'Annotation for %s' % self.object_class


class AnnotatedImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
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

    def __unicode__(self):
        return u'%s' % self.auc
