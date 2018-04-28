from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
# Create your models here.


class FieldModel(models.Model):
    TYPE_OF_FIELD = (
        ('int', 'integer'),
        ('float', 'float'),
        ('str', 'string'),
    )
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    typefield = models.CharField(
        max_length=9, choices=TYPE_OF_FIELD, default='string')
    required = models.BooleanField(default=False)
    array = models.BooleanField(default=False)
    array_length = models.IntegerField(default=10)
    range_start = models.IntegerField()
    range_end = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ObjModel(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    field = models.ManyToManyField(
        FieldModel, blank=True, verbose_name="list of fields")
    array = models.BooleanField(default=False)
    array_length = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ApiModel(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    field = models.ManyToManyField(
        FieldModel, blank=True, verbose_name="list of fields")
    obj = models.ManyToManyField(
        ObjModel, blank=True, verbose_name="list of objs")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


    """ddd
     """
class ProjectModel(models.Model):
    created = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    api = models.ManyToManyField(
        ApiModel, blank=True, verbose_name="list of apis")

    def __str__(self):
        return "%s %s" % (self.name, self.api)

    class Meta:
        ordering = ('name',)
