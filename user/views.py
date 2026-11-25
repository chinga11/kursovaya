from django.shortcuts import render
from django.contrib.auth import login
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("post_list")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
