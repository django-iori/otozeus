from django.db import models

# Create your models here.

class Demo(models.Model):
    video = models.FileField(upload_to='uploads/')