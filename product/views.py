from django.shortcuts import render,get_object_or_404,redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Favorite, Product
from .forms import CommentForm, ProductForm
from django.db.models import Q
# def index(request):
#     products=Product.objects.all()
#     products_pone =Product.objects.filter(name='phone')
#     return render(request, 'products/product.html')

def hello_world(r):
    return HttpResponse("Hello world")

def my_name(r):
    name = "Chynga"
    return HttpResponse(f"<h1> Hello </h1> {name}")

def say_name(r,name):
    return HttpResponse(f"<h1> Hello </h1> {name} ")

def post_list(request: HttpRequest):
    qp = request.GET
    posts = Product.objects.filter()
    if search:= qp.get("search"):
        name = Q(name__icontains=search)
        description = Q(description__icontains=search)
        posts = posts.filter(name | description)
    
    favorite_product_ids = set()
    if request.user.is_authenticated:
        favorite_product_ids = set(
            Favorite.objects.filter(user=request.user).values_list("product_id", flat=True)
        )
    return render(request, "products/product.html", {
        "products": posts,
        "search": qp.get("search", ""),
        "favorite_product_ids": favorite_product_ids,
    })

def post_detail(r,pk):
    product = get_object_or_404(Product, id=pk)
    comment_form = CommentForm()
    is_favorite = r.user.is_authenticated and Favorite.objects.filter(
        user=r.user, product=product
    ).exists()
    return render(r, "products/detail_product.html", {
        "product": product,
        "comments": product.comments.select_related("user").all(),
        "comment_form": comment_form,
        "is_favorite": is_favorite,
    })


@login_required
def add_comment(request: HttpRequest, pk: int) -> HttpResponse:
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
    return redirect("detail_product", pk=product.pk)


@login_required
def toggle_favorite(request: HttpRequest, pk: int) -> HttpResponse:
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
        if not created:
            favorite.delete()
    destination = request.POST.get("next")
    if destination == "cart":
        return redirect("cart")
    if destination == "post_list":
        return redirect("post_list")
    return redirect("detail_product", pk=product.pk)


@login_required
def favorites_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.filter(favorited_by__user=request.user).select_related(
        "category", "user"
    )
    return render(request, "products/favorites.html", {
        "products": products,
    })

# def create_post(request: HttpRequest) -> HttpRequest:
#     if request.method.lower() == "post":
#         data = {
#             "name": request.POST["name"],
#             "description": request.POST["description"],
#             "image": request.FILES.get("image"),
#         }
#         product = Product.objects.create(**data)
#         return redirect("detail_product", pk=product.pk)
#     return render(request,"products/create_post.html")

@login_required
def create_post(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            form.save_m2m()
            return redirect("detail_product", pk=product.pk)
    else:
        form = ProductForm()
    return render(request, "products/create_post.html", {"form": form, "is_edit": False})

@login_required
def edit_post(request: HttpRequest, pk: int) -> HttpResponse:
    product = get_object_or_404(Product, id=pk, user=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("detail_product", pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, "products/create_post.html", {"form": form, "product": product, "is_edit": True})

@login_required
def delete_post(request: HttpRequest, pk: int) -> HttpResponse:
    product = get_object_or_404(Product, id=pk, user=request.user)
    if request.method.lower() == "post":
        product.delete()
        return redirect("post_list")
    return render(request, "products/delete_post.html", {"product": product})
