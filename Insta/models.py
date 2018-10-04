from django.db import models

# Create your models here.
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/')
    bio = HTMLField()




class Image(models.Model):
    name = models.CharField(max_length =30,null=True)
    caption = models.TextField(null=True)
    likes = models.TextField(null=True)
    comments = models.TextField(null=True)
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