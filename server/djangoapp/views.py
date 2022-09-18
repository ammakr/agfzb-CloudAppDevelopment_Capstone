from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from .forms import RegisterForm

# Get an instance of a logger
logger = logging.getLogger(__name__)

def about(request):
    if request.method == "GET":
        return render(request, "djangoapp/about.html")


def contact(request):
    if request.method == "GET":
        return render(request, "djangoapp/contact.html")


def registration_request(request):  
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect("/djangoapp")
    else:
        form = RegisterForm()
            
    return render(request, "registration.html", {"form": form})

def login_request(request):
    return redirect("/djangoapp")

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

