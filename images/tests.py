from unicodedata import category, name
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

class ImagesTestClass(TestCase):
    def setUp(self):
        self.wildlife = Category(name = "Wildlife")
        self.wildlife.save_category()

        self.newYork = Location(location = 'NewYork')
        self.newYork.save_location()

        self.new_image = Images(name = 'Ruweydha', image = 'image.png', description = 'This is a random test' , location = self.newYork, category = self.wildlife) 

    def test_instance(self):
        self.assertTrue(self.new_image, Images)  

    def tearDown(self):
        Images.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()      

    def test_save_image(self):
        self.new_image.save_image() 
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)   

    def test_delete_method(self):
        self.newYork.delete_location()
        images = Images.objects.all()
        self.assertTrue(len(images)==0)   

    def test_get_image_by_id(self) :
         self.new_image.save_image()
         image = Images.get_image_by_id(self.new_image.id)
         self.assertTrue(image ,self.new_image) 

    def test_search_by_category(self):
        self.new_image.save_image()
        images = Images.search_image_by_category(self.new_image.category)   
        self.assertTrue(len(images)>0)  
    
    def test_filter_by_location(self):
        self.new_image.save_image()
        images = Images.filter_by_location(self.new_image.location)   
        self.assertTrue(len(images)>0) 

    def test_update_image(self):
        self.new_image.save_image()
        new_image = 'Ruweydha.png' 
        self.new_image.update_image(new_image)
        self.assertEqual(self.new_image.image, new_image)
