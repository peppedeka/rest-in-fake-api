from rest_framework import serializers
from .models import ProjectModel, ApiModel
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = '__all__'