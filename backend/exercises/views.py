import random
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Categories, Exercises, Methods, Types, Subcategories, Subtypes
from django.views.generic import ListView, DetailView
import re

from django.http import JsonResponse
import subprocess
import pexpect
# ------------------- Helper functions -------------------
# To get a content list based on the description
def parse_description(description):
    paragraphs = description.split('\n')
    content_element = ""
    list_element = []
    for paragraph in paragraphs:
        if re.match(r'^\d+\.\s', paragraph):
            list_element.append(paragraph)
        else:
            content_element += paragraph + "\n"
    return content_element.strip(), list_element

# To get a category and exercise based on the name
def get_category_and_exercise(category_name, exer_title=None):
    category = get_object_or_404(Categories, name=category_name)
    if exer_title:
        exercise = get_object_or_404(Exercises, title=exer_title)
        return category, exercise
    return category, None

# To get the code running
def execute_code(code, language, input_data):
    match language:
        case 'python':
            child = pexpect.spawn('python3 -c "{}"'.format(code.replace('"', '\\"')))
        case 'cpp':
            compile_process = subprocess.Popen(['g++', '-o', 'program', '-x', 'c++', '-'], 
                                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                                               stderr=subprocess.PIPE)
            compile_process.communicate(input=code.encode())
            child = pexpect.spawn('./program')
        case _:
            return 'Unsupported language'
    
    while True:
        try:
            index = child.expect(['Input:', pexpect.EOF])  # Wait for the script to output 'Input:' or end
            if index == 0:  # If the script output 'Input:'
                if input_data:
                    child.sendline(input_data)  # Send the input
                    input_data = None  # Clear the input data
                else:
                    return 'Input required'  # Return 'Input required' if there's no input data
            else:  # If the script ended
                return child.before.decode()  # Return the output of the script
        except pexpect.TIMEOUT:  # If the script doesn't output anything for a while
            return 'Input required'  # Return 'Input required'
        
def execute_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('lang')
        input_data = request.POST.get('input')
        result = execute_code(code, language, input_data)
        if result == 'Input required':
            return JsonResponse({'result': 'Input required'})
        else:
            return JsonResponse({'result': result})
    else:
        return JsonResponse({'result': 'Invalid request'})
# ------------------- Views -------------------
# Home page
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
#----------------------------------------------
# Types
class TypesView(ListView):
    model = Types
    template_name = "types.html"
    context_object_name = 'tipos'
    
class TypeDetailView(DetailView):
    model = Types
    template_name = 'type_detail.html'
    context_object_name = 'type'
    slug_field = 'name'
    slug_url_kwarg = 'type_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subtypes = Subtypes.objects.filter(type=self.object)
        context.update({
            'subtypes': subtypes
        })
        return context

class SubTypeDetailView(DetailView):
    model = Subtypes
    template_name = 'subtype_detail.html'
    context_object_name = 'subtype'
    slug_field = 'name'
    slug_url_kwarg = 'subtype_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = Types.objects.get(name=self.kwargs['type_name'])
        context.update({
            'type': type
        })
        return context
#----------------------------------------------
# Differences
class DifferencesView(ListView):
    model = Methods
    template_name = "differences.html"
    context_object_name = 'methods'

class DifferencesDetailView(DetailView):
    model = Methods
    template_name = 'differences_detail.html'
    context_object_name = 'method'
    slug_field = 'func'
    slug_url_kwarg = 'method_name'
#----------------------------------------------
# Categories
class CategoriesView(ListView):
    model = Categories
    template_name = "categories.html"
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'category_detail.html'
    context_object_name = 'category'
    slug_field = 'name'
    slug_url_kwarg = 'category_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise = Exercises.objects.filter(category=self.object)
        random_exercise = random.choice(list(exercise))
        textExam, objectives = parse_description(random_exercise.desc)
        textCat, steps = parse_description(self.object.content)
        subcategories = Subcategories.objects.filter(category=self.object)
        context.update({
            'exercise': random_exercise,
            'textCat': textCat,
            'steps': steps,
            'text': textExam,
            'objectives': objectives,
            'subcategories': subcategories
        })
        return context
    
class SubcategoriesDetailView(DetailView):
    model = Subcategories
    template_name = 'subcategory_detail.html'
    context_object_name = 'subcategory'
    slug_field = 'name'
    slug_url_kwarg = 'subcategory_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category, _ = get_category_and_exercise(self.kwargs['category_name'])
        exercise = Exercises.objects.filter(category=category, subcategoty=self.object)
        random_exercise = random.choice(list(exercise))
        textExam, objectives = parse_description(random_exercise.desc)
        textCat, steps = parse_description(self.object.content)
        context.update({
            'category': category,
            'exercise': random_exercise,
            'textCat': textCat,
            'steps': steps,
            'text': textExam,
            'objectives': objectives
        })
        return context
#----------------------------------------------
# Exercises
class ExercisesView(ListView):
    model = Categories
    template_name = "exercises.html"
    context_object_name = 'categories'

class ExerciseListView(ListView):
    model = Exercises
    template_name = 'exercise_list.html'
    context_object_name = 'exercise'

    def get_queryset(self):
        self.category, _ = get_category_and_exercise(self.kwargs['category_name'])
        return Exercises.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class ExerciseDetailView(DetailView):
    model = Exercises
    template_name = 'exercise_detail.html'
    context_object_name = 'exercise'

    def get_object(self):
        category, exercise = get_category_and_exercise(self.kwargs['category_name'], self.kwargs['exer_title'])
        return exercise

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        text, objectives = parse_description(self.object.desc)
        context.update({
            'category': self.kwargs['category_name'],
            'text': text,
            'objectives': objectives
        })
        return context