import misaka # Allows mark-down text in text inputs
from django.db import models
from django.utils.text import slugify # formats url strings by removing spaces and adding dashes to make the string url format compatible.
from django.core.urlresolvers import reverse

from django.contrib.auth import get_user_model
User = get_user_model()  # Get the current user

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag (Use custom template tags)
from django import template
register = template.Library()


class Group(models.Model):
	''' The group model '''
	
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(allow_unicode=True, unique=True)
	description = models.TextField(blank=True, default='')
	description_html = models.TextField(editable=False, default='', blank=True)
	members = models.ManyToManyField(User, through='GroupMember')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		self.description_html = misaka.html(self.description)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('groups:single', kwargs={'slug':self.slug})


	class Meta:
		ordering = ['name']


class GroupMember(models.Model):
	''' Links the current 'User' to a 'Group'. This class is related to django's User model via the 'user' attr called 'user_groups' and is also related to the 'Group' model via the 'group' attr called 'memberships' '''

	group = models.ForeignKey(Group, related_name='memberships')
	user = models.ForeignKey(User, related_name='user_groups')

	def __str__(self):
		return self.user.username  # default django User Model has a username attr + others

	class Meta:
		unique_together = ('group', 'user')
