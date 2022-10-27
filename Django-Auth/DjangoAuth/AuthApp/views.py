from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

@login_required(login_url="/login")
def HomePage(request):
    return render(request, "home.html")


def UserRegister(request):
    print(request.POST)
    if request.POST:
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]

        if pass1 == pass2:
            user = authenticate(email, pass1)
            if user in not None:

        else:
            return render(request, "register.html", {"msg": "Passwords don't match"})

def UserLogin(request):
    pass

def UserLogout(request):
    pass
