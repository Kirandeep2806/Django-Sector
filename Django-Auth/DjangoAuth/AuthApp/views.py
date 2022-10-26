from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def HomePage(request):
    return render(request, "home.html")


