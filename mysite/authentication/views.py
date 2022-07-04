from django.shortcuts import render

from operator import truediv
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

import authentication
from .password_generator import passGen
from .forms import LoginForm

def pass_gen(request):
    msg = None
    success = False
    form = LoginForm(request.POST)
    if request.method == "POST":
        form = LoginForm(request.POST)
        fullName = request.POST["fullName"]
        password = request.POST["password"]
        siteDomain = request.POST["siteDomain"]
        msg = passGen(fullName, password, siteDomain)
        form.fullName = " "
        form.siteDomain = " "

    # redirect("/register/")
    return render(request, "login.html", {"form": form, "msg": msg, "success": success})

def pass_generated(request):
    msg = None
    success = False
    form = LoginForm(request.POST)
    if request.method == "POST":
        form = LoginForm(request.POST)
        fullName = request.POST["fullName"]
        password = request.POST["password"]
        siteDomain = request.POST["siteDomain"]
        msg = passGen(fullName, password, siteDomain)
        form.fullName = " "
        form.siteDomain = " "

    # redirect("/register/")
    return render(request, "pass.html", {"form": form, "msg": msg, "success": success})