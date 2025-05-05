"""
URL configuration for TiendaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from miapp.views import CustomAuthToken
from miapp import views

urlpatterns = [
    # Páginas principales
    path('', views.inicio),
    path('Index/', views.inicio, name='Index'),
    path('Registro/', views.Registro, name='Registro'),
    path('Perfil/', views.Perfil, name='Perfil'),
    path('PerfilAdmin/', views.PerfilAdmin, name='PerfilAdmin'),

    # Carrito de compras
    path('Carro/', views.Carro, name='Carro'),
    path('agregar/<int:producto_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('eliminar/<int:producto_id>/', views.eliminar_prod_al_carro, name='eliminar_del_carro'),

    # Autenticación
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),

    # Categorías y productos
    path('categorias/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('juego/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

    # APIs
    path('api/juegos/', views.juegos_api_externa, name='juegos_api_externa'),
    path('api/ofertas/', views.ofertas_juegos_api_externa, name='ofertas_juegos_api_externa'),
    path('api/productos/lista/', views.productos_api_lista, name='productos_api_lista'),
    path('perfil/redirect/', views.redireccionar_perfil, name='redireccionar_perfil'),

    # Administración
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),

    path('api/token/', CustomAuthToken.as_view(), name='api_token_auth'),

    # Gestión de usuarios
    path('gestion/usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('gestion/usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('gestion/usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('gestion/usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Gestión de productos
    path('gestion/productos/', views.listar_productos, name='listar_productos'),
    path('gestion/productos/crear/', views.crear_producto, name='crear_producto'),
    path('gestion/productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('gestion/productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # APIs
    path('api/juegos/', views.juegos_api_externa, name='juegos_api_externa'),
    path('api/ofertas/', views.ofertas_juegos_api_externa, name='ofertas_juegos_api_externa'),
    path('api/productos/lista/', views.productos_api_lista, name='productos_api_lista'),
    path('perfil/redirect/', views.redireccionar_perfil, name='redireccionar_perfil'),


    # Gestión de usuarios
    path('gestion/usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('gestion/usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('gestion/usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('gestion/usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Gestión de productos
    path('gestion/productos/', views.listar_productos, name='listar_productos'),
    path('gestion/productos/crear/', views.crear_producto, name='crear_producto'),
    path('gestion/productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('gestion/productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    #Carrito de compras
    path('Carro/', views.Carro, name='Carro'),
    path('agregar/<int:producto_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_del_carro'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
]