# encoding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.

def public_add(request):
    return render(request,
                  "website/home.html",
                  )
    
