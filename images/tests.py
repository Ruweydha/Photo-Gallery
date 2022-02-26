from json import load
from sre_parse import CATEGORIES
from unicodedata import name
from django.test import TestCase
from .models import Category, Location, Images

# Create your tests here.

class CategoryTestClass(TestCase):
    def setUp(self):
        self.wildlife = Category(name = 'Wildlife')

    def test_instance(self):
        self.assertTrue(isinstance(self.wildlife, Category))  

    def test_save_method(self):
        self.wildlife.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)    

    def test_delete_method(self):
        self.wildlife.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)==0)      
    

class LocationTestClass(TestCase):
    def setUp(self):
        self.newYork = Location(location = 'NewYork')   

    def test_instance(self):
        self.assertTrue(self.newYork, Location)  

    def test_save_location(self):
        self.newYork.save_location()  
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)  

    def test_delete_method(self):
        self.newYork.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)         

        