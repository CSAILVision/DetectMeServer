from django.db import models
from detectors.models import Detector


class Performance(models.Model):
    """
    Stores performance metrics for the detector.
    Calculated outside with a test set.
    """
    created_at = models.DateTimeField(auto_now=True)
    detector = models.ForeignKey(Detector)
    average_precision = models.FloatField()
    precision = models.TextField(blank=True, null=True)
    recall = models.TextField(blank=True, null=True)
    test_set = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # creates the UserScore entry
        super(Performance, self).save(*args, **kwargs)
        name = self.detector.name
        try:
            category = Category.objects.get(name=name.split("_")[0])
        except Category.DoesNotExist:
            category = Category.objects.get(name="NA")
        user_score = UserScore(user=self.detector.author, category=category)
        user_score.save()
    
    def __unicode__(self):
        return u'Performance of %s - %s by %s is %s' % (self.detector.name,
                                                        self.detector.pk,
                                                        self.detector.author.username,
                                                        self.average_precision)


class Category(models.Model):
    name = models.CharField(max_length=50)

    @property
    def detectors(self):
        """
        Returns all the detectors associated with that category
        """
        detectors = Detector.objects.filter(name__startswith=self.name)
        return detectors

    def __unicode__(self):
        return u'%s' % self.name


class UserScore(models.Model):
    """
    Summarizes participants of the competition results
    """
    user = models.ForeignKey('accounts.DetectMeProfile')
    category = models.ForeignKey(Category)

    @property
    def detectors(self):
        detectors = self.category.detectors
        detectors = detectors.filter(author=self.user)
        return detectors

    @property
    def max_score(self):
        detectors = self.detectors
        
        max_score = detectors[0].performance.average_precision
        for detector in detectors:
            if detector.performance.average_precision > max_score:
                max_score = detector.performance.average_precision
        return max_score

    def __unicode__(self):
        return u'%s: %s' % (self.user.username, self.max_score)
