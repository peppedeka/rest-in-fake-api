from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import ProjectModel, ApiModel, FieldModel, ObjModel


class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjModel
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    def validate(self, data):
        print(data)
        range_s = data['range_start']
        range_e = data['range_end']
        if range_s > range_e:
            raise ValidationError('range end < of range start')
        return data

    class Meta:
        model = FieldModel
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = '__all__'

