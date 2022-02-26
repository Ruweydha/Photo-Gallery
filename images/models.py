from distutils.command.upload import upload
from pydoc import describe
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class  Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Images(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=150)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    date_posted = models.DateField(auto_now_add = True)
