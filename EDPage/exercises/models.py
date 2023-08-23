from django.db import models

# Create your models here.

class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

    def __str__(self):
        return f"ID: {self.cat_id}, Name: {self.name}"


class Exercises(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    cpp_snippet = models.TextField()
    py_snippet = models.TextField()

    def __str__(self):
        return f"Category: {self.category.name}, Title: {self.title}, Description: {self.desc}, Cpp Code: {self.cpp_snippet}, Py Code: {self.py_snippet}"
