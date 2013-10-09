from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver
import uuid


class Detector(models.Model):
    name = models.CharField(max_length=50)
    target_class = models.CharField(max_length=50)
    author = models.ForeignKey('accounts.DetectMeProfile')
    is_public = models.BooleanField(default=False)
    average_image = models.ImageField(upload_to='average_image/',
                                      default='average_image/default.jpg')
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    weights = models.TextField()  # arrays to be serialized with JSON
    sizes = models.TextField()
    support_vectors = models.TextField()
    is_deleted = models.BooleanField(default=False)
    hash_value = models.CharField(max_length=32, blank=True,
                                  editable=False, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)

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
    created_at = models.DateTimeField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    image_jpeg = models.ImageField(upload_to='annotated_images/',
                                   default='average_image/default.jpg')
    image_height = models.PositiveSmallIntegerField(editable=False, blank=True)
    image_width = models.PositiveSmallIntegerField(editable=False, blank=True)
    box_x = models.FloatField()
    box_y = models.FloatField()
    box_height = models.FloatField()
    box_width = models.FloatField()
    author = models.ForeignKey('accounts.DetectMeProfile', editable=False)
    detector = models.ForeignKey(Detector)

    def save(self, *args, **kwargs):
        # im = Image.open(self.image_jpeg.path)
        self.image_width = 3  # im.size[0]
        self.image_height = 3  # im.size[1]
        super(AnnotatedImage, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.image_jpeg.name


# Delete image files when deleting objects from the database
@receiver(post_delete, sender=Detector)
def detector_post_delete_handler(sender, **kwargs):
    detector = kwargs['instance']
    storage, path = detector.average_image.storage, detector.average_image.path
    storage.delete(path)


@receiver(post_delete, sender=AnnotatedImage)
def annotatedImage_post_delete_handler(sender, **kwargs):
    annotatedImage = kwargs['instance']
    storage, path = (annotatedImage.image_jpeg.storage,
                     annotatedImage.image_jpeg.path)
    storage.delete(path)
