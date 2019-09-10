from django.db import models
from django.contrib import auth

class User(auth.models.User, auth.models.PermissionsMixin):
	''' User model, models specs from default django user model '''
	
	def __str__(self):
		return '@{}'.format(self.username)