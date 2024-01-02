from django.shortcuts import render


import battle.forms as forma

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def login(request):
    context = {}
    # if request.method == 'POST':
    #     f = forma.Autor(request.POST)
    #     context["form"] = f
    #     if f.is_valid():
    #         log = f.data["login"]
    #         context["errors"] = []
    #         context["ec"] = 0
    #         pw = f.data["password"]
    #         user = authenticate(username=log, password=pw, request=request)
    #         if user is not None:
    #             lin(request, user=user)
    #         else:
    #             context["errors"].append("LogInv")
    #             context["ec"] += 1
    #         return redirect('/')
    #         # return render(request, 'registration/login.html', context)
    #
    # else:
    #     context["form"] = forma.Autor()

    return render(request, 'login.html', context)


def registration(request):
    context = {}
    return render(request, 'registration.html', context)
# Create your views here.
