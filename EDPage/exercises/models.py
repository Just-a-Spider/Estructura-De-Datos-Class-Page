from django.db import models

# Create your models here.

class Types(models.Model):
    name = models.CharField(max_length=20)
    traduc = models.CharField(max_length=25, default='traduccion')
    content = models.TextField(default='texto')
    def __str__(self):
        return f"Name: {self.name}"

class Categories(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=150, default='set-iconify-here')
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
    
class Methods(models.Model):
    func = models.CharField(max_length=25)
    detail = models.TextField()
    py_snip = models.TextField()
    cpp_snip = models.TextField()

    def __str__(self):
        return f'Theme: {self.func}'
