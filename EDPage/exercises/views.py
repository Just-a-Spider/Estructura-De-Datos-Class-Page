import random
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Categories, Exercises, Methods, Types
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
            compile_process = subprocess.Popen(['g++', '-o', 'program', '-x', 'c++', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            compile_process.communicate(input=code.encode())
            child = pexpect.spawn('./program')
        case _:
            return 'Unsupported language'
    child.sendline(input_data)
    child.expect(pexpect.EOF)
    return child.before.decode()

@csrf_exempt
def execute_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('lang')
        input_data = request.POST.get('input')
        if input_data is None:
            input_data = ''
        if code is None or language is None:
            return JsonResponse({'error': 'code or language is missing'})
        result = execute_code(code, language, input_data)
        return JsonResponse({'result': result})
# ------------------- Views -------------------
# Home page
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
#----------------------------------------------
# Types
class TypesView(View):
    def get(self, request):
        type_list = Types.objects.all()
        return render(request, 'types.html', {'tipos': type_list})
class TypeDetailView(View):
    def get(self, request, type_name):
        type = get_object_or_404(Types, name=type_name)
        return render(request, 'type_detail.html', {'type': type})
#----------------------------------------------
# Differences
class DifferencesView(View):
    def get(self, request):
        method_list = Methods.objects.all()
        return render(request, "differences.html", {'methods': method_list})
class DifferencesDetailView(View):
    def get(self, request, method_name):
        method = get_object_or_404(Methods, func=method_name)
        return render(request, 'differences_detail.html', {'method': method})
#----------------------------------------------
# Categories
class CategoriesView(View):
    def get(self, request):
        categories_list = Categories.objects.all()
        return render(request, 'categories.html', {'categories': categories_list})
class CategoryDetailView(View):
    def get(self, request, category_name):
        category, _ = get_category_and_exercise(category_name)
        exercise = Exercises.objects.filter(category=category)
        random_exercise = random.choice(exercise)
        textExam, objectives = parse_description(random_exercise.desc)
        textCat, steps = parse_description(category.content)
        return render(request, 'category_detail.html', {'category': category, 'exercise': random_exercise,'textCat':textCat, 'steps':steps, 'text':textExam, 'objectives':objectives})
#----------------------------------------------
# Exercises
class ExercisesView(View):
    def get(self, request):
        categories_list = Categories.objects.all()
        return render(request, "exercises.html", {'categories': categories_list})
class ExerciseListView(View):
    def get(self, request, category_name):
        category, _ = get_category_and_exercise(category_name)
        exercise = Exercises.objects.filter(category=category)
        return render(request, 'exercise_list.html', {'category': category, 'exercise': exercise})
class ExerciseDetailView(View):
    def get(self, request, category_name, exer_title):
        category, exercise = get_category_and_exercise(category_name, exer_title)
        text, objectives = parse_description(exercise.desc)
        return render(request, 'exercise_detail.html', {'category':category_name,'exercise':exercise, 'text':text, 'objectives':objectives})