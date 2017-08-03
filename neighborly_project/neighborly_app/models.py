from django.db import models

# Create your models here.
class User(models.Model):
	state = models.CharField(max_length=2)
	city = models.CharField(max_length=30)



