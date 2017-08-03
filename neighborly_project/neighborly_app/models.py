from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=2)
	zip_code = models.IntegerField()
	



