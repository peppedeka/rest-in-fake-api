from django.db import models
from datetime import datetime
# Create your models here.


class ApiModel(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ProjectModel(models.Model):
    created = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    api = models.ManyToManyField(ApiModel, verbose_name="list of apis")

    def __str__(self):
        return "%s %s" % (self.name, self.api)

    class Meta:
        ordering = ('name',)
