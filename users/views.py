from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        login_form = UserLoginForm()
    context = {
        "login_form": login_form,
    }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(register_form.non_field_errors)
    else:
        register_form = UserRegistrationForm()

    context = {
        "register_form": register_form
    }
    return render(request, 'users/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def profile(request):
    if request.method == "POST":
        profile_form = UserProfileForm(data=request.POST,  files=request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        profile_form = UserProfileForm(instance=request.user)
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'users/profile.html', context)