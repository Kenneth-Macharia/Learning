from django.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^users/', views.users, name='users'),
	re_path(r'^register/', views.user_reg, name='user_reg')
]