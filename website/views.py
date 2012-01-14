# encoding: utf-8
from django.shortcuts import render
from public.models import Public


def home(request, page=1):
    "Starting page without login"
    must_popular_public_list = Public.objects.must_popular(page=page)
    last_public_list = Public.objects.lastest_five()

    return render(request,
                  "website/home.html",
                  {
                   "must_popular_public_list":must_popular_public_list,
                   "last_public_list":last_public_list,
                   }
                  )


def novidades(request):
    "News without login"
    return render(request, "base.html")


def institucional(request):
    "Institucional without login"
    return render(request, "base.html")


def termos(request):
    "Termo without login"
    return render(request, "base.html")


def contato(request):
    "Contato without login"
    return render(request, "base.html")
