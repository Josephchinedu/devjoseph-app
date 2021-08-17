from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    # p_image = models.ImageField(upload_to='p_photos/%Y')
    project_name = models.CharField(max_length=300)
    project_tag = models.CharField(max_length=100)
    project_url = models.URLField()
    project_published = models.BooleanField(default=True)
    project_desc = models.TextField(blank=True, null=True)
    project_lang = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self) -> str:
        return self.project_name


class Profile(models.Model):
    image = CloudinaryField('image', blank=True, null=True)
