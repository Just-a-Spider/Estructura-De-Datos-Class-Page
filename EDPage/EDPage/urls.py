from django.contrib import admin
from django.urls import path

from exercises.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('Datos/', TypesView.as_view(), name='tipos'),
    path('Datos/<str:type_name>/', TypeDetailView.as_view(), name='tipos_detail'),
    path('Datos/<str:type_name>/<str:subtype_name>/', SubTypeDetailView.as_view(), name='subtipos_detail'),
    path('Diferencias/', DifferencesView.as_view(), name='diferencia'),
    path('Diferencias/<str:method_name>', DifferencesDetailView.as_view(), name = 'diferencias_detail' ),
    path('Temas/', CategoriesView.as_view(), name='temas'),
    path('Temas/<str:category_name>/', CategoryDetailView.as_view(), name='categoria'),
    path('Temas/<str:category_name>/<str:subcategory_name>/', SubcategoriesDetailView.as_view(), name='subcategoria'),
    path('Ejercicios/', ExercisesView.as_view(), name='ejercicios'),
    path('Ejercicios/<str:category_name>/', ExerciseListView.as_view(), name='lista'),
    path('Ejercicios/<str:category_name>/<str:exer_title>/', ExerciseDetailView.as_view(), name='ejemplo'),
    #path('ejecutar/', execute_code_view, name='ejecutar'),
    path('admin/', admin.site.urls),
]