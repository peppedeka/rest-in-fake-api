from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from .models import ProjectModel


urlpatterns = [
    url(r'^project/$', views.projectList.as_view()),
    url(r'^project/(?P<pk>[a-z0-9]+)/$', views.projectDetail.as_view()),
]

projects = ProjectModel.objects.all()

for project in projects:
    print(project)
    apis = project.api.all()
    for api in apis:
        urlpatterns.append(url(
            r'^' + project.name + '/(?P<pk>[a-z0-9]+)/$', views.apiOfProjectList.as_view()))

urlpatterns.append(url(r'^api/$', views.apiList.as_view()))
urlpatterns.append(
    url(r'^api/(?P<pk>[a-z0-9]+)/$', views.apiDetail.as_view()),)
urlpatterns.append(url(r'^field/$', views.fieldList.as_view()))
urlpatterns.append(
    url(r'^field/(?P<pk>[a-z0-9]+)/$', views.fieldDetail.as_view()),)
urlpatterns.append(url(r'^obj/$', views.objList.as_view()))
urlpatterns.append(
    url(r'^obj/(?P<pk>[a-z0-9]+)/$', views.objDetail.as_view()),)

urlpatterns = format_suffix_patterns(urlpatterns)
