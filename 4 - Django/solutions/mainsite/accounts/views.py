from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request, 'accounts/register.html')

def createuser(request):

    username = request.POST['username']
    email_address = request.POST['email_address']
    password = request.POST['password']

    if User.objects.filter(username=username).exists():
        return render(request, 'accounts/register.html', {'message':'username already exists'})

    user = User.objects.create_user(username=username, email=email_address, password=password)
    login(request, user)
    return render(request, 'accounts/profile.html')


def loginpage(request):
    return render(request, 'accounts/login.html')

def loginuser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('accounts:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('accounts:profile'))


# def profile(request):
#     if request.user.is_authenticated:
#         return render(request, 'accounts/profile.html')
#     else:
#         return HttpResponseRedirect(reverse('accounts:register'))


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
