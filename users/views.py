from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm

def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(data = request.POST)
        print(login_form)
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
    return render(request, 'users/register.html')