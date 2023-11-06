from django.contrib import admin
from django.urls import path

from exercises.views import *

urlpatterns = [
    path('', DifferencesView.as_view(), name='inicio'),
    path('datos/', TypesView.as_view(), name='tipos'),
    path('datos/<str:type_name>/', TypeDetailView.as_view(), name='tipos_detail'),
    path('diferencias/', DifferencesView.as_view(), name='diferencia'),
    path('diferencias/<str:method_name>', DifferencesDetailView.as_view(), name = 'diferencias_detail' ),
    path('temas/', CategoriesView.as_view(), name='temas'),
    path('temas/<str:category_name>/', CategoryDetailView.as_view(), name='categoria'),
    path('ejercicios/', ExercisesView.as_view(), name='ejercicios'),
    path('ejercicios/<str:category_name>/', ExerciseListView.as_view(), name='lista'),
    path('ejercicios/<str:category_name>/<str:exer_title>/', ExerciseDetailView.as_view(), name='ejemplo'),
    path('admin/', admin.site.urls),
]