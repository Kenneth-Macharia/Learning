from django.contrib import admin
from . import models

class GroupMemberInLine(admin.TabularInline):
	''' Allows editing of models from the same page as the parent modelin the admin page, thus foregoing explicit registration of the model with the admin interface '''

	model = models.GroupMember

admin.site.register(models.Group)
