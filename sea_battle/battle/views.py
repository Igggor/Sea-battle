from django.shortcuts import render
from django.http import HttpResponse


import battle.forms as forma

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as lin
from django.contrib.auth import logout as lout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required(redirect_field_name="gg", login_url="login")
def index(request):
    context = {}
    return render(request, 'index.html', context)


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
                    return render(request, 'login.html', context)
                return redirect('/')
            else:
                context["errors"].append("LogInv")
                print("No such user")

    else:
        context["form"] = forma.Login()

    return render(request, 'login.html', context)


def logout(request):
    context = {}
    lout(request)
    # print(request.user.is_authenticated) #Проверка, зареган ли пользователь
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
            pw = f.data["password"]
            pw_d = f.data["password_double"]
            if User.objects.filter(username=log).exists():
                context["errors"].append("Exists")
            else:
                if pw == pw_d:
                    user = User.objects.create_user(username=log, password=pw)
                    user.save()
                    return redirect('/')
                else:
                    context["errors"].append("FD_pass")

    else:
        context["form"] = forma.Registration()

    return render(request, 'registration.html', context)
