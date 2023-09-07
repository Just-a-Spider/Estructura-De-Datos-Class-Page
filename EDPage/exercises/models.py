from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=15)
    summary = models.TextField(default='resumen')
    content = models.TextField(default='texto')

    def __str__(self):
        return f"Name: {self.name}, Summary: {self.summary}"


class Exercises(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    cpp_snippet = models.TextField()
    py_snippet = models.TextField()

    def __str__(self):
        return f"Category: {self.category.name}, Title: {self.title}"
