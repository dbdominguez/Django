from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroUsuarioForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')
# General.
def inicio(request):
    return render(request, "Index.html")

def Registro(request):
    return render(request, "Registro.html")

def Perfil(request):
    return render(request, "Perfil.html")

def Carro(request):
    return render(request, "Carro.html")


# Categorias.
def visualnovel(request):
    return render(request, "visual-novel.html")

def survivalhorror(request):
    return render(request, "survival-horror.html")

def simuladores(request):
    return render(request, "simuladores.html")

def rol(request):
    return render(request, "rol.html")

def estrategia(request):
    return render(request, "estrategia.html")

def deporte(request):
    return render(request, "deporte.html")

def arcadeclasicos(request):
    return render(request, "arcade-clasicos.html")


# Juegos.
def DanganronpaV3(request):
    return render(request, "DanganronpaV3.html")

def AceAttorneyTriology(request):
    return render(request, "AceAttorneyTriology.html")

def Silenthill2R(request):
    return render(request, "Silenthill2R.html")

def ResidentEvil2R(request):
    return render(request, "ResidentEvil2R.html")

def StardewValley(request):
    return render(request, "StardewValley.html")

def MicrosoftFlightSimulator(request):
    return render(request, "MicrosoftFlightSimulator.html")

def Persona5(request):
    return render(request, "Persona5.html")

def KingdomHearts3(request):
    return render(request, "KingdomHearts3.html")

def CivilizationVI(request):
    return render(request, "CivilizationVI.html")

def AoE2D(request):
    return render(request, "AoE2D.html")

def NBA2K24(request):
    return render(request, "NBA2K24.html")

def MarioStrikers(request):
    return render(request, "MarioStrikers.html")

def VirtuaFighter5(request):
    return render(request, "VirtuaFighter5.html")

def PacManMuseum(request):
    return render(request, "PacManMuseum.html")
