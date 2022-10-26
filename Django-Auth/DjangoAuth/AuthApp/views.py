from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required("/login")
def HomePage(request):
    return render(request, "home.html")

def UserLogin(request):
    pass

def UserLogout(request):
    pass

def UserRegister(request):
    pass
