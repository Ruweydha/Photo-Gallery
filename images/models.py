from distutils.command.upload import upload
from pydoc import describe
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()
    
    def delete_category(self):
        Category.objects.filter(id = self.id).delete()

    def update_category(self, updates):
         Category.objects.filter(id = self.id).update(name = updates)
 

    def __str__(self):
        return self.name

class  Location(models.Model):
    location = models.CharField(max_length=30)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        Location.objects.filter(id = self.id).delete()

    def __str__(self):
        return self.location

class Images(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=150)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    date_posted = models.DateField(auto_now_add = True)
