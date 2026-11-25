from django.contrib import admin
from product.models import Category, Comment, Favorite, Product, Tag

admin.site.register([Product, Category, Tag, Comment, Favorite])
    
