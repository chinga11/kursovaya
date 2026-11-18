from django.forms import ModelForm
from .models import Product
from django import forms
# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'category', 'tags', 'image']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "tags", "image"]
        labels = {
            "name": "Название",
            "description": "Описание",
            "category": "Категория",
            "tags": "Теги",
            "image": "Фото",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-select"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control", "accept": "image/*"}),
        }