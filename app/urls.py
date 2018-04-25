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
for project in projects:
    print(project)
    apis = project.api.all()
    for api in apis:
        urlpatterns.append( url(r'^' + project.name + '/(?P<pk>[a-z0-9]+)/$', views.apiOfProjectList.as_view()),)

urlpatterns.append(url(r'^api/$', views.apiList.as_view()))
urlpatterns.append(url(r'^api/(?P<pk>[a-z0-9]+)/$', views.apiDetail.as_view()),)
urlpatterns.append(url(r'^field/$', views.fieldList.as_view()))
urlpatterns.append(url(r'^field/(?P<pk>[a-z0-9]+)/$', views.fieldDetail.as_view()),)
urlpatterns = format_suffix_patterns(urlpatterns)
