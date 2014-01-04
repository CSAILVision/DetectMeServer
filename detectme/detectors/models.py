from datetime import datetime
import uuid
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


class Detector(models.Model):
    name = models.CharField(max_length=50)
    target_class = models.CharField(max_length=50)
    author = models.ForeignKey('accounts.DetectMeProfile')
    is_public = models.BooleanField(default=False)
    average_image = models.ImageField(upload_to='average_image/',
                                      default='defaults/default.png',
                                      null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    weights = models.TextField()  # arrays to be serialized with JSON
    sizes = models.TextField()
    is_deleted = models.BooleanField(default=False)
    hash_value = models.CharField(max_length=32, blank=True,
                                  editable=False, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    @property
    def average_rating(self):
        """
        Returns the average rating for the detector
        """
        ratings = self.rating_set.all()
        if len(ratings) is 0:
            return 0

        sum_ratings = 0
        for rating in ratings:
            sum_ratings = sum_ratings + rating.rating

        return sum_ratings * 1.0 / len(ratings)

    @property
    def number_ratings(self):
        return len(self.rating_set.all())

    @property
    def number_images(self):
        return len(self.annotatedimage_set.all())

    @property
    def support_vectors(self):
        return self.extrainfo.support_vectors

    def save(self, *args, **kwargs):
        if not self.hash_value:
            self.hash_value = uuid.uuid1().hex
        if not self.created_at:
            self.created_at = datetime.now()
        super(Detector, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s - %s: %s class by %s' % (self.name, self.pk, self.target_class,
                                        self.author.user)

    class Meta:
        ordering = ('created_at',)


@receiver(post_delete, sender=Detector)
def detector_post_delete_handler(sender, **kwargs):
    """
    Delete associated image when deleting a detector
    """
    detector = kwargs['instance']
    storage, path = detector.average_image.storage, detector.average_image.path
    storage.delete(path)


@receiver(post_save, sender=Detector)
def save_extra_info(sender, instance, signal, created, **kwargs):
    """
    Save extra info after creating a detector.
    """
    if created:
        instance.extrainfo.detector = instance
        instance.extrainfo.save()


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
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    motion_quaternionX = models.FloatField()
    motion_quaternionY = models.FloatField()
    motion_quaternionZ = models.FloatField()
    motion_quaternionW = models.FloatField()
    author = models.ForeignKey('accounts.DetectMeProfile', editable=False)
    detector = models.ForeignKey(Detector)

    def save(self, *args, **kwargs):
        self.image_width = self.image_jpeg.width
        self.image_height = self.image_jpeg.height
        super(AnnotatedImage, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.image_jpeg.name


@receiver(post_delete, sender=AnnotatedImage)
def annotatedImage_post_delete_handler(sender, **kwargs):
    """
    Delete associated images when deleting a detector
    """
    annotatedImage = kwargs['instance']
    storage, path = (annotatedImage.image_jpeg.storage,
                     annotatedImage.image_jpeg.path)
    storage.delete(path)


class Rating(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('accounts.DetectMeProfile')
    detector = models.ForeignKey(Detector)
    rating = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return u'%s rated %s by %s' % (self.author.user, self.detector.name, self.rating)


class ExtraInfo(models.Model):
    """
    Stores heavy information from the detector. Prevents big detector tables.
    """
    detector = models.OneToOneField(Detector)
    support_vectors = models.TextField()
    training_log = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'Extra info for %s' % (self.detector.name)


# class Performance(models.Model):
#     """
#     Stores performance metrics for the detector.
#     Calculated outside with a test set.
#     """
#     created_at = models.DateTimeField(auto_now=True)
#     detector = models.ForeignKey(Detector)
#     average_precision = models.FloatField()
#     precision = models.TextField(blank=True, null=True)
#     recall = models.TextField(blank=True, null=True)
#     test_set = models.TextField(blank=True, null=True)

#     def __unicode__(self):
#         return u'Performance of %s - %s by %s is %s' % (self.detector.name,
#                                                         self.detector.pk,
#                                                         self.detector.author.username,
#                                                         self.average_precision)




