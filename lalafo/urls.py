"""
URL configuration for lalafo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import hello_world,post_detail
from product.views import my_name,say_name,post_list,create_post,delete_post
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from django.contrib.auth.views import LoginView
from user.views import register
urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_world),
    path("name/", my_name),
    path("name/<str:name>", say_name),
    path("",post_list,name='post_list'),
    path("product/<int:pk>/", post_detail, name="detail_product"),
    path("product/create/",create_post,name="create_post"),
    path("product/<int:pk>/delete/", delete_post, name="delete_post"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)