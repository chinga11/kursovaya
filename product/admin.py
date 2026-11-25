from django.contrib import admin
from product.models import Category, Product, Tag

admin.site.register([Product, Category, Tag])
    
