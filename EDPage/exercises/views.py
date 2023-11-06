import random
from django.shortcuts import render, get_object_or_404
from .models import Categories, Exercises, Methods, Types
#-------------------------------------------------------------------------------
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
def home(request):
    return render(request, 'home.html')
#-------------------------------------------------------------------------------
# Types Views.
def types(request):
    type_list = Types.objects.all()
    return render(request, 'types.html',
                  {'tipos': type_list})
def type_detail(request, type_name):
    type = get_object_or_404(Types, name=type_name)
    return render(request, 'type_detail.html',
                  {'type': type})
#-------------------------------------------------------------------------------
# Differences Views.
def differences(request):
    method_list = Methods.objects.all()
    return render(request, "differences.html", 
                  {'methods':method_list})
def differences_view(request, method_name):
    method = get_object_or_404(Methods, func=method_name)
    return render(request, 'differences_detail.html',
                  {'method': method})
#-------------------------------------------------------------------------------
# Themes Views.
def topics_view(request):
    categories_list = Categories.objects.all()
    return render(request, 'categories.html', 
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
