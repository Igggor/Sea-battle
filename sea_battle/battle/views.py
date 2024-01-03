from django.shortcuts import render
from django.http import HttpResponse


import battle.forms as forma
from battle.models import *

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
                    profile = Profile(user=user, is_admin=False)
                    profile.save()
                    return redirect('/')
                else:
                    context["errors"].append("FD_pass")

    else:
        context["form"] = forma.Registration()

    return render(request, 'registration.html', context)


@login_required(redirect_field_name="gg", login_url="login")
def clear_bd(request):
    data = User.objects.all()
    for el in data:
        el.delete()
    return HttpResponse("Cleared")


@login_required(redirect_field_name="gg", login_url="login")
def check_bd(request):
    data = User.objects.all()
    # print(request.user.profile.is_admin) #Проверка, Админ ли пользователь
    s = ""
    for el in data:
        s += f'<p>{str(el.profile.id)}</p>'
    return HttpResponse(s)


@login_required(redirect_field_name="gg", login_url="login")
def profile(request):
    user = request.user
    context = {
        'name': user.username,
        'admForm': forma.BecomeAdmin(),
        'nameForm': forma.ChangeLogin(),
        'passForm': forma.ChangePassword(),

    }
    if request.user.profile.is_admin:
        return render(request, "Admin_Profile.html", context)
    else:
        return render(request, "User_Profile.html", context)


@login_required(redirect_field_name="gg", login_url="login")
def amin(request):
    uuu = request.user
    user = Profile.objects.filter(user=uuu).update(is_admin=not request.user.profile.is_admin)
    return render(request, "index.html", context={})
