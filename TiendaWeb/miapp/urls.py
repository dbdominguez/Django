from django.urls import path
from . import views

urlpatterns = [
    path('api/productos/', views.api_productos, name='api_productos'),
    path('api/categorias/', views.api_categorias, name='api_categorias'),
]