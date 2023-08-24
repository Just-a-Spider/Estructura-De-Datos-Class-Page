from django.shortcuts import render
from .models import Categories
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def topics_view(request, *args, **kwargs):
    categories_list = Categories.objects.all()
    return render(request, "temas.html", {'categories': categories_list})


def exercises_view(request, *args, **kwargs):
    categories_list = Categories.objects.all()
    return render(request, "exercises.html", {'categories': categories_list})
