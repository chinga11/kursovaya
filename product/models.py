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


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_comments")
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Комментарий {self.user.username} к {self.product.name}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "product"], name="unique_user_favorite_product"),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"


# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     text = models.CharField()
#     rate = models.IntegerField()
