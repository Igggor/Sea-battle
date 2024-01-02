from django.shortcuts import render
from django.http import HttpResponse


import battle.forms as forma

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def index(request):
    print(request.user.is_authenticated)
    context = {}
    return HttpResponse("return this string")


def login(request):
    context = {}
    if request.method == 'POST':
        f = forma.Login(request.POST)
        context["form"] = f
        if f.is_valid():
            log = f.data["login"]
            context["errors"] = []
            context["ec"] = 0
            pw = f.data["password"]
            if User.objects.filter(username=log).exists():
                user = authenticate(username=log, password=pw, request=request)
                if user is not None:
                    lin(request, user=user)
                else:
                    context["errors"].append("LogInv")
                    context["ec"] += 1
                    print("None")
                return redirect('/')
            else:
                print("No such user")

    else:
        context["form"] = forma.Login()

    return render(request, 'login.html', context)


def registration(request):
    context = {}
    if request.method == 'POST':
        f = forma.Registration(request.POST)
        context["form"] = f
        if f.is_valid():
            log = f.data["login"]
            context["errors"] = []
            context["ec"] = 0
            pw = f.data["password"]
            pw_d = f.data["password_double"]
            if User.objects.filter(username=log).exists():
                print("User already exist")
            else:
                if pw == pw_d:
                    user = User.objects.create_user(username=log, password=pw)
                    user.save()
                    print("Ok")
                    return redirect('/')
                else:
                    print("first pass != doubled pass")

    else:
        context["form"] = forma.Registration()

    return render(request, 'registration.html', context)
