from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length =30,null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)

    def __str__(self):
        return self.bio

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    
     

    # def update_image(self):
    #     self.update()




class Image(models.Model):
    name = models.CharField(max_length =30,null=True)
    caption =  HTMLField()
    likes = models.CharField(max_length =30,null=True)
    commnts =models.CharField(max_length =30,null=True)
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')


    def __str__(self):
        return self.user.username

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ["-id"]

    @classmethod
    def upl(cls):
        uploads = cls.objects.all()
        return uploads

    # def update_caption(self):
    #     self.update()

class Comment(models.Model):
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(User,related_name='comments',null=True)
    post = models.ForeignKey(Image,related_name='comments',null=True)

    def __str__(self):
        return self.comment
