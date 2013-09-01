from django.db import models

# Create your models here.

class Box(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	xcoord = models.FloatField()
	ycoord = models.FloatField()
	detector = models.CharField(max_length=200)

	def __unicode__(self):
		return u'%s (%s,%s)' % (self.detector, str(self.xcoord), str(self.ycoord))
