from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import Usuario, Producto
from .forms import RegistroUsuarioForm, ProductoForm, PerfilUsuarioForm
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

def Registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rol_id = 2 
            usuario.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

 

def login_usuario(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        user = authenticate(request, correo=correo, password=password)
        if user is not None:
            login(request, user)
            # Redireccionar según el rol
            if user.rol.nombre == "Administrador":
                return redirect('PerfilAdmin') 
            else:
                return redirect('Perfil')
        else:
            messages.error(request, "Correo o contraseña inválidos.")
            return redirect('Index')
    else:
        return redirect('Index')
    

def logout_usuario(request):
    logout(request)
    return redirect('login')

def recuperar_contrasena(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        Usuario = get_user_model()
        try:
            Usuario = Usuario.objects.get(correo=correo)
            messages.success(request, f'Se ha enviado un enlace de recuperación a {correo}.')
        except Usuario.DoesNotExist:
            messages.error(request, 'El correo ingresado no está registrado.')
        return redirect('Index')

def solo_admins(user):
    return user.is_authenticated and user.rol.nombre == "Administrador"


def agregar_al_carro(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carro = request.session.get('carrito', {})
    carro[str(producto_id)] = carro.get(str(producto_id), 0) + 1
    request.session['carro'] = carro
    return redirect('carro')
    
# General.
def inicio(request):
    return render(request, "Index.html")

def registro_usuario(request):
    return render(request, "Registro.html")

@login_required
def Perfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('Perfil')
    else:
        form = PerfilUsuarioForm(instance=usuario)

    return render(request, "Perfil.html", {
        'form': form,
        'usuario': usuario
    })

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

# API EXTERNA
def juegos_api_externa(request):
    url = 'https://api.rawg.io/api/games'
    params = {
        'key': '446b53a8039f4f14911502bea09dbe8d',
        'page_size': 6,
    }
    response = requests.get(url, params=params)
    juegos = response.json().get('results', [])

    return render(request, 'juegos_api.html', {'juegos': juegos})


# API PROPIA
def productos_api_lista(request):
    productos = Producto.objects.all()
    return render(request, 'productos_api.html', {'productos': productos})

# REDIRECCION
@login_required
def redireccionar_perfil(request):
    if request.user.rol.nombre == "Administrador":
        return redirect('PerfilAdmin')
    else:
        return redirect('Perfil')

# ADMIN
@login_required
@user_passes_test(solo_admins)
def PerfilAdmin(request):
    return render(request, "PerfilAdmin.html", {"usuario": request.user})


# USUARIOS 
@login_required
@user_passes_test(solo_admins)
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

@login_required
@user_passes_test(solo_admins)
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'formulario_usuarios.html', {'form': form})

@login_required
@user_passes_test(solo_admins)
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'formulario_usuarios.html', {'form': form})

@login_required
@user_passes_test(solo_admins)
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listar_usuarios')


# PRODUCTOS
@login_required
@user_passes_test(solo_admins)
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

@login_required
@user_passes_test(solo_admins)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'formulario_productos.html', {'form': form})

@login_required
@user_passes_test(solo_admins)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'formulario_producto.html', {'form': form})

@login_required
@user_passes_test(solo_admins)
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    producto.delete()
    return redirect('listar_productos')