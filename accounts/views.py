from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect("home")
    return render(request, "accounts/login.html", {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "accounts/logout.html")


def register_view(request):
    pass
