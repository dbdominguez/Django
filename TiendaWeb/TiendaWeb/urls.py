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
    path('Carro/', views.Carro, name='Carro'),

    path('visual-novel/', views.visualnovel, name='visual-novel'),
    path('survival-horror/', views.survivalhorror, name='survival-horror'),
    path('simuladores/', views.simuladores, name='simuladores'),
    path('rol/', views.rol, name='rol'),
    path('estrategia/', views.estrategia, name='estrategia'),
    path('deporte/', views.deporte, name='deporte'),
    path('arcade-clasicos/', views.visualnovel, name='arcade-clasicos'),

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

    path('admin/', admin.site.urls),
]
