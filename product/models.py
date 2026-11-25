from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    

class Category(models.Model):
    name=models.CharField()
    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name=models.CharField()
    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    name= models.CharField(max_length=64)
    description = models.TextField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tags=models.ManyToManyField(Tag,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to="product")
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return f"{self.name}"


# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     text = models.CharField()
#     rate = models.IntegerField()
