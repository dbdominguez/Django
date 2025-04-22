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
from django.urls import path
from miapp import views

urlpatterns = [
    path('', views.inicio),
    path('Index/', views.inicio, name='Index'),
    path('Registro/', views.Registro, name='Registro'),
    path('Perfil/', views.Perfil, name='Perfil'),
    path('PerfilAdmin/', views.PerfilAdmin, name='PerfilAdmin'),

    path('Carro/', views.Carro, name='Carro'),
    path('agregar/<int:producto_id>/', views.agregar_al_carro, name='agregar_al_carro'),

    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),

    path('visual-novel/', views.visualnovel, name='visual-novel'),
    path('survival-horror/', views.survivalhorror, name='survival-horror'),
    path('simuladores/', views.simuladores, name='simuladores'),
    path('rol/', views.rol, name='rol'),
    path('estrategia/', views.estrategia, name='estrategia'),
    path('deporte/', views.deporte, name='deporte'),
    path('arcade-clasicos/', views.arcadeclasicos, name='arcade-clasicos'),

    path('DanganronpaV3/', views.DanganronpaV3, name='DanganronpaV3'),
    path('AceAttorneyTriology/', views.AceAttorneyTriology, name='AceAttorneyTriology'),
    path('Silenthill2R/', views.Silenthill2R, name='Silenthill2R'),
    path('ResidentEvil2R/', views.ResidentEvil2R, name='ResidentEvil2R'),
    path('StardewValley/', views.StardewValley, name='StardewValley'),
    path('MicrosoftFlightSimulator/', views.MicrosoftFlightSimulator, name='MicrosoftFlightSimulator'),
    path('Persona5/', views.Persona5, name='Persona5'),
    path('KingdomHearts3/', views.KingdomHearts3, name='KingdomHearts3'),
    path('CivilizationVI/', views.CivilizationVI, name='CivilizationVI'),
    path('AoE2D/', views.AoE2D, name='AoE2D'),
    path('NBA2K24/', views.NBA2K24, name='NBA2K24'),
    path('MarioStrikers/', views.MarioStrikers, name='MarioStrikers'),
    path('VirtuaFighter5/', views.VirtuaFighter5, name='VirtuaFighter5'),
    path('PacManMuseum/', views.PacManMuseum, name='PacManMuseum'),

    path('api/juegos/', views.juegos_api_externa, name='juegos_api_externa'),
    path('api/productos/lista/', views.productos_api_lista, name='productos_api_lista'),
    path('perfil/redirect/', views.redireccionar_perfil, name='redireccionar_perfil'),

    path('admin/', admin.site.urls),

    path('gestion/usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('gestion/usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('gestion/usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('gestion/usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('gestion/productos/', views.listar_productos, name='listar_productos'),
    path('gestion/productos/crear/', views.crear_producto, name='crear_producto'),
    path('gestion/productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('gestion/productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
