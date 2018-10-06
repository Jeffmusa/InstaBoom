from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Image,Profile
from django.contrib.auth.models import User


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date','comments','likes']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pro_photo', 'bio')
       

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')