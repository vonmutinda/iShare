from django.test import TestCase
from .models import Image , Location , Category

'''
Image tests using TestCase module
'''
class ImageTestClass(TestCase):

    def setUp(self):
        self.location = Location(name = 'Shengzhen')
        self.location.save()

        self.category= Category(name='Exuberance')
        self.category.save()

        self.image= Image(name = 'Coffee', description ='Developers love coffee',location=self.location,category = self.category)
        self.image.save_image()


    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))


    def test_can_save_image(self):
        self.image.save_image()
        images = Image.fetch_all()
        self.assertTrue(len(images)>0)


    def test_can_search(self):
        self.image.save_image()
        image = Image.search_image('coffee')
        self.assertTrue(len(image)>0)
    
    def test_can_fetch_all_images(self):
        self.image.save_image()
        images = Image.fetch_all()
        self.assertTrue(len(images)==1)

    def test_can_get_by_category(self):
        self.image.save_image()
        images = Image.get_by_category('Exuberance')
        self.assertTrue(len(images)>0)

    def test_can_get_by_location(self):
        self.image.save_image()
        images = Image.get_by_location('Shengzhen')
        self.assertTrue(len(images)>0)


    def test_can_update_image(self):
        self.image.save_image()
        image = Image.objects.filter(name = "Coffee").update(name = "Caffeine")
        self.assertTrue(image,"Caffeine")


    def test_can_delete_images(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.fetch_all()
        self.assertTrue(len(images)==0)