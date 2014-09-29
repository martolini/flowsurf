from django.db import models

class Subscriber(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	message = models.TextField()

	def __unicode__(self):
		return u'%s' % self.name
