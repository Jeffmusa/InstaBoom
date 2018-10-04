from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.Img= Image(name = 'Jeff', caption='Made with love')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Img,Image))

    def test_save_method(self):
        self.Img.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_data(self):
        self.assertTrue(self.Img.name,"test")

    def test_delete(self):
        post = Image.objects.filter(id=1)
        post.delete()
        posts = Image.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Img.save()
        posts = Image.objects.get(id=1)
        self.assertTrue(posts.name,'kol')

class ProfileTestClass(TestCase):

    def setUp(self):
        self.Pro= Profile(bio = 'Jeff')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Profile))


    def test_delete(self):
        pro = Profile.objects.filter(id=1)
        pro.delete()
        cat = Profile.objects.all()
        self.assertTrue(len(cat)==0)

    def test_save_method(self):
        self.Pro.save_image()
        pros = Profile.objects.all()
        self.assertTrue(len(pros) > 0)




