from django.urls import re_path
from . import views

app_name = 'cbvs_app' 

urlpatterns = [
    re_path(r'^$', views.SchoolListView.as_view(), name='list'), # name is for idying the url 																 in the html template tag.
    re_path(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'), # (?P<pk>\d+) 																				 represents the 																			 primary key of a 																			   model value.
    re_path(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete')
]