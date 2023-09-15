from django.contrib import admin
from .models import Categories, Exercises, Methods

# Register your models here.

admin.site.register(Categories)
admin.site.register(Exercises)
admin.site.register(Methods)

