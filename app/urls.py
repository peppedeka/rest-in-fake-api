from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from .models import ProjectModel
import logging

logger = logging.getLogger(__name__)
logger.error('Something went wrong!')
try:
    projects = ProjectModel.objects.all()
except ValueError:
    project = []

urlpatterns = [
    url(r'^project/$', views.projectList.as_view()),
    url(r'^project/(?P<pk>[0-9]+)/$', views.projectDetail.as_view()),
]
"""for project in projects:
    urlpatterns.append( url(r'^' + project.name + '/', views.apiOfProjectList.as_view()),)
"""
urlpatterns.append(url(r'^api/$', views.apiList.as_view()))
urlpatterns = format_suffix_patterns(urlpatterns)
