import random
from django.shortcuts import render, get_object_or_404
from .models import Categories, Exercises

# Extract elements of the models.descriptions
import re

def parse_description(description):
    # Split the description into paragraphs
    paragraphs = description.split('\n')

    # Initialize variables to store the content and list elements
    content_element = ""
    list_element = []

    # Iterate through the paragraphs
    for paragraph in paragraphs:
        # Check if the paragraph starts with a digit followed by a period
        if re.match(r'^\d+\.\s', paragraph):
            list_element.append(paragraph)
        else:
            content_element += paragraph + "\n"

    return content_element.strip(), list_element
#-------------------------------------------------------------------------------
# Home Views.
def home_view(request):
    return render(request, "index.html", {})
#-------------------------------------------------------------------------------
# Themes Views.
def topics_view(request):
    categories_list = Categories.objects.all()
    return render(request, "temas.html", 
                  {'categories': categories_list})

def category_detail(request, category_name):
    category = get_object_or_404(Categories, name=category_name)
    exercise = Exercises.objects.filter(category=category)
    random_exercise = random.choice(exercise)
    textExam, objectives = parse_description(random_exercise.desc)
    textCat, steps = parse_description(category.content)
    return render(request, 'category_detail.html',
                  {'category': category, 'exercise': random_exercise,'textCat':textCat, 'steps':steps, 
                   'text':textExam, 'objectives':objectives})
#--------------------------------------------------------------------------------
# Exercises Views
def exercises_view(request):
    categories_list = Categories.objects.all()
    return render(request, "exercises.html", 
                  {'categories': categories_list})

def exercise_list(request, category_name):
    category = get_object_or_404(Categories, name=category_name)
    exercise = Exercises.objects.filter(category=category)
    return render(request, 'exercise_list.html', 
                  {'category': category, 'exercise': exercise})

def exercise_detail(request, category_name, exer_title):
    exercise = get_object_or_404(Exercises, title= exer_title)
    text, objectives = parse_description(exercise.desc)
    return render(request, 'exercise_detail.html', 
                  {'category':category_name,'exercise':exercise, 'text':text, 'objectives':objectives})
#--------------------------------------------------------------------------------
