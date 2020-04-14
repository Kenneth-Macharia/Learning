from django.urls import re_path
from . import views

# App name space for template tagging
app_name = 'templates_app'

urlpatterns = [
    re_path(r'^relative/', views.relative, name='relative'),
    re_path(r'^other/', views.other, name='other')
]