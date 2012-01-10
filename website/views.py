# encoding: utf-8
from django.shortcuts import render

def home(request):
    "Starting page without login"
    return render("base.html")
