from django.contrib import admin
from . import models


class MovieAdmin(admin.ModelAdmin):
	''' This class named as "yourModelAdmin"  ovewrites the display order of your model fields. Default order is as defined in the model class, here we define a list of the field names in the order we like them displayed in the admin page '''

	fields = ['release_year', 'title', 'length']

	# add search fields, being abilty to search for model data using the model fields
	search_fields = ['title', 'length']

	# add filter fields
	list_filter = ['release_year', 'length']

	# add fields to display in the model list view
	list_display = ['title', 'release_year', 'length']

	# add the editable fields in list view
	list_editable = ['length']


# The above class alongside the model it relates to
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)

