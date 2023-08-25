import random
from django.shortcuts import render, get_object_or_404
from .models import Categories, Exercises

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def topics_view(request, *args, **kwargs):
    categories_list = Categories.objects.all()
    return render(request, "temas.html", {'categories': categories_list})

def category_detail(request, category_name):
    category = get_object_or_404(Categories, name=category_name)
    exercise = Exercises.objects.filter(category=category)
    random_exercise = random.choice(exercise)
    return render(request, 'category_detail.html', {'category': category, 'exercise': random_exercise})


def exercises_view(request, *args, **kwargs):
    categories_list = Categories.objects.all()
    return render(request, "exercises.html", {'categories': categories_list})


def exercise_list(request, category_name):
    category = get_object_or_404(Categories, name=category_name)
    exercise = Exercises.objects.filter(category=category)
    return render(request, 'exercise_list.html', {'category': category, 'exercise': exercise})

def exercise_detail(request, category_name, exer_title):
    category = category_name
    exercise = get_object_or_404(Exercises, title= exer_title)
    return render(request, 'exercise_detail.html', {'category':category_name,'exercise':exercise})
