from django.shortcuts import render
from .models import Categories
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    categories_list = Categories.objects.all()
    #return HttpResponse("<h1>Inicio</h1>")
    return render(request, "index.html", {'categories': categories_list})

def topics_view(request, *args, **kwargs):
    return HttpResponse("<h1>Acerca de la pagina</h1>")


def exercises_view(request, *args, **kwargs):
    return HttpResponse("<h1>Acerca de la pagina</h1>")
