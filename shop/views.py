import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import user
from .models import genders


def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
#
#
#
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        inn = request.POST["inn"]
        gender = genders.objects.get(gender=request.POST["gender"])
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })
        if first_name == '' or last_name == '' or inn == "":
            return render(request, 'register.html', {
                'message': "Заполните пожалуйста все поля."
            })

        # Attempt to create new user
        try:
            User = user.objects.create_user(email, email, password)
            User.save()
            User.first_name = first_name
            User.last_name = last_name
            User.inn = inn
            User.gender = gender
            #User.is_active = False
            User.save()
        except IntegrityError as e:
            print(e)
            return render(request, "register.html", {
                "message": "Email address already taken."
            })
        login(request, User)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

