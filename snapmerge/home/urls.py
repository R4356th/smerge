from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^open_project/$', views.OpenProjectView.as_view(), name='open_proj'),
    url(r'^create_project/$', views.CreateProjectView.as_view(), name='create_proj'),
    url(r'^(?P<proj_id>[0-9]+)$', views.ProjectView.as_view(), name='proj'),
    url(r'^merge/(?P<proj_id>[0-9]+)$', views.MergeView.as_view(), name='merge'),
    url(r'^sync/(?P<proj_id>[0-9]+)$', views.SyncView.as_view(), name='sync'),
    url(r'add/(?P<proj_id>[0-9]+)$',views.AddFileToProjectView.as_view(), name='add')
]