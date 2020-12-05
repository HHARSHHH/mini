from django.db import models

# Create your models here.
class products(models.Model):
	title = models.CharField(max_length=20)
	disc = models.TextField()
