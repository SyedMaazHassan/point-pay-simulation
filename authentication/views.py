from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import get_messages
from authentication.forms import *
from authentication.supporting_func import *

# Create your views here.


def index(request):
    return redirect("authentication:login")


def register(request):
    if request.user.is_authenticated:
        return redirect("simulation:index")
    return render(request, "authentication/register.html")


def login(request):
    print("abc")
    if request.user.is_authenticated:
        return redirect("simulation:index")
    context = {
        "form": LoginForm(
            initial={"username": "SyedEibadHassan", "password": "eibad143143"}
        )
    }
    return render(request, "accounts/login.html", context)


def login_submit(request):
    if request.method == "POST":
        form_check = formIsValid(request, ["username", "password"])
        if form_check["status"]:
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session["user_course"] = {}
                return redirect("simulation:index")
            else:
                messages.error(request, "Entered credentials is incorrect!")
        else:
            messages.error(request, form_check["message"])
    else:
        messages.error(request, "Invalid request")

    # all_msgs = get_messages(request)
    # for i in all_msgs:
    #     print(i.level)
    # # print(all_msgs)

    return redirect("authentication:login")


def logout(request):
    auth.logout(request)
    return redirect("authentication:login")
