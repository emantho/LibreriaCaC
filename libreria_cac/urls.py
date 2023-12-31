"""
URL configuration for libreria_cac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from .views import IndexPage
from .views import LibrosPage
from .views import CategoriasPage
from .views import CarritoPage
from .views import LoginPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPage.as_view(), name="index"),
    path("libros", LibrosPage.as_view(), name="libros"),
    path("categorias/", CategoriasPage.as_view(), name="categorias"),
    path("carrito", CarritoPage.as_view(), name="carrito"),
    path("login", LoginPage.as_view(), name="login"),
    path("libro/", include("app_libreria.urls")),
]
