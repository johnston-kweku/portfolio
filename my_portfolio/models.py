from django.db import models
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='project_pic/')
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    description = models.TextField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
