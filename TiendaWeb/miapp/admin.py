#Antiguo
'''
from django.contrib import admin
from .models import Usuario, Producto, Categoria, Carrito, ItemCarrito, Compra, DetalleCompra

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
'''


#editado
from django.contrib import admin
from .models import Categoria, Juego, Perfil, Orden, OrdenItem, Valoracion

admin.site.register(Categoria)
admin.site.register(Juego)
admin.site.register(Perfil)
admin.site.register(Orden)
admin.site.register(OrdenItem)
admin.site.register(Valoracion)
