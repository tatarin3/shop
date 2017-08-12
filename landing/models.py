from django.db import models

# Create your models here.
class Subscr(models.Model):
	"""docstring for Subscr"""
	email = models.EmailField()
	name = models.CharField(max_length=128)
		