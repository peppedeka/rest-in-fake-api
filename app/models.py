from django.db import models
from datetime import datetime
# Create your models here.
class ProjectModel(models.Model):
    created = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=100,unique=True)

    class Meta:
        ordering = ('created','name')