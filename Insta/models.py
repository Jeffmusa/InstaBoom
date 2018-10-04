from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/')
    bio = models.TextField(null=True)

    def __str__(self):
        return self.bio

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()




class Image(models.Model):
    name = models.CharField(max_length =30,null=True)
    caption =  HTMLField()
    likes = models.CharField(max_length =30,null=True)
    comments =models.CharField(max_length =30,null=True)
    profile = models.ForeignKey(Profile, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()