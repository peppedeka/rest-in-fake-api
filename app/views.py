from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProjectModel, ApiModel
from .serializer import ProjectSerializer, ApiSerializer


class projectList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    serializer_class = ProjectSerializer

    def get(self, request, format=None):
        projects = ProjectModel.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class projectDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    serializer_class = ProjectSerializer

    def get_object(self, pk):
        try:
            return ProjectModel.objects.get(pk=pk)
        except ProjectModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class apiOfProjectList(APIView):
    serializer_class = ApiSerializer

    def get(self, request, format=None):
        api = self.get_object(pk)
        serializer = ApiSerializer(api)
        return Response(serializer.data)


class apiList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    serializer_class = ApiSerializer

    def get(self, request, format=None):
        api = ApiModel.objects.all()
        serializer = ApiSerializer(api, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class apiDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    serializer_class = ApiSerializer

    def get_object(self, pk):
        try:
            return ApiModel.objects.get(pk=pk)
        except ApiModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        api = self.get_object(pk)
        serializer = ApiSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        api = self.get_object(pk)
        serializer = ApiSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        api = self.get_object(pk)
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
