"""
URL configuration for EDPage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from exercises.views import *

urlpatterns = [
    path('', differences, name='inicio'),
    path('datos/', types, name='tipos'),
    path('datos/<str:type_name>/', type_detail, name='tipos_detail'),
    path('run-code/', run_code, name='run_code'),
    path('diferencias/', differences, name='diferencia'),
    path('diferencias/<str:method_name>', differences_view, name = 'diferencias_detail' ),
    path('temas/', topics_view, name='temas'),
    path('temas/<str:category_name>/', category_detail, name='categoria'),
    path('ejercicios/', exercises_view, name='ejercicios'),
    path('ejercicios/<str:category_name>/', exercise_list, name='lista'),
    path('ejercicios/<str:category_name>/<str:exer_title>/', exercise_detail, name='ejemplo'),
    path('admin/', admin.site.urls),
]
