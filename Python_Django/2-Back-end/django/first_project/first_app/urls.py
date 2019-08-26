from django.urls import re_path
from . import views


# Have the app host its own urls and call them from the projects urls.py file.
urlpatterns = [
	re_path(r'^$', views.index, name='index')

]
