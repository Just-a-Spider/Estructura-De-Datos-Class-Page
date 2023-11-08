from django.db import models

# Create your models here.

class Types(models.Model):
    name = models.CharField(max_length=25)
    traduc = models.CharField(max_length=25, default='traduccion')
    content = models.TextField(default='texto')
    hasSubtypes = models.BooleanField(default=False)
    def __str__(self):
        return f"Tipo: {self.name}"
    
class Subtypes(models.Model):
    name = models.CharField(max_length=25)
    traduc = models.CharField(max_length=25, default='traduccion')
    content = models.TextField(default='texto')
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    def __str__(self):
        return f"Subtipo: {self.name}"

class Categories(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=150, default='set-iconify-here')
    summary = models.TextField(default='resumen')
    content = models.TextField(default='texto')
    hasSubcategories = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.name}"
    
class Subcategories(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=150, default='set-iconify-here')
    summary = models.TextField(default='resumen')
    content = models.TextField(default='texto')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f"Subcategories: {self.name}"

class Exercises(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    cpp_snippet = models.TextField()
    py_snippet = models.TextField()
    subcategoty = models.ForeignKey(Subcategories, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f"Category: {self.category.name}, Title: {self.title}"
    
class Methods(models.Model):
    func = models.CharField(max_length=25)
    detail = models.TextField()
    py_snip = models.TextField()
    cpp_snip = models.TextField()

    def __str__(self):
        return f'Theme: {self.func}'
