from django.shortcuts import render
from time import strftime
# from django.http import HttpResponse


def home(request):
    return render(request, "main/home.html", {'date': strftime("%A, %B %d %Y")})
