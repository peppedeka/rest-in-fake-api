from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from random import randint

from .models import ProjectModel, ApiModel, FieldModel, ObjModel
from .serializer import ProjectSerializer, ApiSerializer, FieldSerializer, ObjSerializer


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

    def get(self, request, pk, format=None):

        api = ApiModel.objects.get(name=pk)
        serializer = ApiSerializer(api, many=True)
        field_data = api.field.all()
        obj_data = api.obj.all()
        jsonResp = {}
        for fld_obj in field_data:
            if (fld_obj.array):
                arrayValue = []
                if fld_obj.typefield == 'int':
                    onetoten = range(0, fld_obj.array_length)
                    for count in onetoten:
                        arrayValue.append(
                            randint(fld_obj.range_start, fld_obj.range_end))
                    jsonResp.update({fld_obj.name: arrayValue})
                elif fld_obj.typefield == 'float':
                    onetoten = range(0, fld_obj.array_length)
                    for count in onetoten:
                        arrayValue.append(
                            randint(fld_obj.range_start, fld_obj.range_end))
                    jsonResp.update({fld_obj.name: arrayValue})
                elif fld_obj.typefield == 'string':
                    onetoten = range(0, fld_obj.array_length)
                    for count in onetoten:
                        arrayValue.append(
                            randint(fld_obj.range_start, fld_obj.range_end))
                    jsonResp.update({fld_obj.name: arrayValue})
            elif fld_obj.typefield == 'int':
                jsonResp.update({fld_obj.name: randint(
                    fld_obj.range_start, fld_obj.range_end)})
            elif fld_obj.typefield == 'float':
                jsonResp.update({fld_obj.name: randint(
                    fld_obj.range_start, fld_obj.range_end)})
            elif fld_obj.typefield == 'string':
                jsonResp.update({fld_obj.name: randint(
                    fld_obj.range_start, fld_obj.range_end)})

        for obj in obj_data:
            jsonFromObjArray = []
            if (obj.array):
                onetoten = range(0, obj.array_length)
                for count in onetoten:
                    jsonFromObj = {}
                    for fld_obj in obj.field.all():
                        if fld_obj.typefield == 'int':
                            jsonFromObj.update({fld_obj.name: randint(
                                fld_obj.range_start, fld_obj.range_end)})
                        elif fld_obj.typefield == 'float':
                            jsonFromObj.update({fld_obj.name: randint(
                                fld_obj.range_start, fld_obj.range_end)})
                        elif fld_obj.typefield == 'string':
                            jsonFromObj.update({fld_obj.name: randint(
                                fld_obj.range_start, fld_obj.range_end)})
                    jsonFromObjArray.append(jsonFromObj)
                jsonResp.update({obj.name: jsonFromObjArray})
            else:
                for fld_obj in obj.field.all():
                    if fld_obj.typefield == 'int':
                        jsonFromObj.update({fld_obj.name: randint(
                            fld_obj.range_start, fld_obj.range_end)})
                    elif fld_obj.typefield == 'float':
                        jsonFromObj.update({fld_obj.name: randint(
                            fld_obj.range_start, fld_obj.range_end)})
                    elif fld_obj.typefield == 'string':
                        jsonFromObj.update({fld_obj.name: randint(
                            fld_obj.range_start, fld_obj.range_end)})
                jsonResp.update({obj.name: jsonFromObj})

        return JsonResponse(jsonResp)

    def post(self, request, format=None):
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        serializer = ApiSerializer(api)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        api = self.get_object(pk)
        serializer = ApiSerializer(api, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        api = self.get_object(pk)
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class fieldList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    serializer_class = FieldSerializer

    def get(self, request, format=None):
        field = FieldModel.objects.all()
        serializer = FieldSerializer(field, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FieldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class fieldDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    serializer_class = FieldSerializer

    def get_object(self, pk):
        try:
            return FieldModel.objects.get(pk=pk)
        except FieldModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        _field = self.get_object(pk)
        serializer = FieldSerializer(_field)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        _field = self.get_object(pk)
        serializer = FieldSerializer(_field, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        _field = self.get_object(pk)
        _field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class objList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    serializer_class = ObjSerializer

    def get(self, request, format=None):
        obj = ObjModel.objects.all()
        serializer = ObjSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObjSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class objDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    serializer_class = ObjSerializer

    def get_object(self, pk):
        try:
            return ObjModel.objects.get(pk=pk)
        except ObjModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        _obj = self.get_object(pk)
        serializer = ObjSerializer(_obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        _obj = self.get_object(pk)
        serializer = ObjSerializer(_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        _obj = self.get_object(pk)
        _obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
