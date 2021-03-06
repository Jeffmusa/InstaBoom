from django.shortcuts import render,redirect
import datetime as dt
from .models import Image,Profile
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,ProfileForm,CommentForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile=Profile(user=user)
            profile.save()            
            current_site = get_current_site(request)
            mail_subject = 'Activate your instagram account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('<h1 style="text-align:center;">Please confirm your email address to complete the registration</h1>')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('welcome')
        return HttpResponse('<h1 style="text-align:center;color:green">Thank you for your email confirmation. To log in to your account follow <a href="/accounts/login">this link </a></h1>.')
        
    else:
        return HttpResponse('Activation link is invalid!')




# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    date = dt.date.today()
    pr = Profile.objects.all()
    comment_form = CommentForm()
    images = Image.objects.all()
    
    return render(request, 'home.html',{"date": date,"comment_form":comment_form, "images":images,"pr":pr})


def profile(request):
    images = Image.objects.all()
    pr = Profile.objects.all()
    profile = Profile.objects.filter(user=request.user)
    current_user = request.user
    posts = Image.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form =ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if image_form.is_valid:
            image_form.save()
        else:
            image_form = ProfileForm()
            return render(request, 'profile.html', {"image_form": image_form,"posts":posts,"profile":profile,"images":images,"pr":pr})
    return render(request, 'profile.html', {"image_form": image_form,"posts":posts,"profile":profile,"images":images})

    

def upload(request):
    # upload = Image.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('/')

    else:
        form = ImageForm()
    return render(request, 'upload.html', {"form": form , "upload": upload})


def comment(request,id):
    upload = Image.objects.get(id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post= upload
            comment.save()
            print(comment)
        return redirect('/')


def search_results(request):    
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.objects.filter(username=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_users": searched_users})

    else:
        message = "Please search for a valid user"
        return render(request, 'search.html',{"message":message,"searched_users":searched_users})

def profiles(request,id):
    profile = Profile.objects.get(user_id=id)
    post=Image.objects.filter(user_id=id)
   
                       
    return render(request,'pros.html',{"profile":profile,"post":post})

def full(request,id):
    post=Image.objects.filter(id=id)
   
                       
    return render(request,'full.html',{"post":post})