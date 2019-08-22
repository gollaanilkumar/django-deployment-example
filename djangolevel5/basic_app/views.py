from django.shortcuts import render
from django import forms
from basic_app.forms import UserForm,UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
    return render(request,'basic_app/index.html')

def registration(request):
    registered=False
    if request.method=="POST":
       user_form=UserForm(data=request.POST)
       user_profile_form=UserProfileForm(data=request.POST)
       if user_form.is_valid() and user_profile_form.is_valid():
           user=user_form.save()
           user.set_password(user.password)
           user.save()

           profile=user_profile_form.save(commit=False)
           profile.user=user
           if 'profile_pic' in request.FILES:
               profile.profile_pic=request.FILES['profile_pic']

           profile.save()
           registered=True
       else:
           print(user_form.errors,user_profile_form.errors)
    else:
        user_form=UserForm()
        user_profile_form=UserProfileForm()

    return render (request,'basic_app/registration.html',{'registered':registered,'UserForm':user_form,'UserProfileForm':user_profile_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login_user(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else :
                return HttpResponse("Acccount not active")

        else :
            print("someone tried to login and failed")
            print("username :{} and password={}").format(username,password)
            return HttpResponse("invalid login details suppplied")
    else:
        return render(request,'basic_app/login.html')



