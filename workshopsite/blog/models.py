from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	titles = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True , null = True )
	

	def published(self):
		published_date = timezone.now()
		self.save()
	def __str__(self):
		return self_title