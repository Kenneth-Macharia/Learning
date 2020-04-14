from django.db import models

# Create your models here.
class User(models.Model):
	''' Model handling user details '''

	First_name = models.CharField(max_length=15)
	Last_name = models.CharField(max_length=15)
	Email = models.EmailField(max_length=50, unique=True)
