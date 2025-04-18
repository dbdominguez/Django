from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]
urlpatterns += [
    path('', views.inicio, name='inicio'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('comprar/', views.procesar_compra, name='procesar_compra'),
    path('historial/', views.historial_compras, name='historial_compras'),
]
