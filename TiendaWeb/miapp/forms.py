#ANTIGUO
'''
from django import forms # Importar el módulo forms de Django
from django.contrib.auth.forms import UserCreationForm # Importar el formulario de creación de usuario, incluyendo la validación de contraseña
from .models import Usuario # Importar el modelo Usuario que hemos creado en models.py


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'rol', 'direccion']

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        # Validaciones de seguridad
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(c.isdigit() for c in password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not any(c.isupper() for c in password):
            raise forms.ValidationError("La contraseña debe tener al menos una letra mayúscula.")
        if not any(c in "!@#$%^&*()_+-=[]{}|;':,.<>?/~`" for c in password):
            raise forms.ValidationError("La contraseña debe tener al menos un caracter especial.")
        return password


'''

#EDITADO
import re
from django import forms
from .models import Usuario, Producto, Rol
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmar_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'direccion', 'telefono', 'password']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.password = make_password(self.cleaned_data['password'])

        # Asignar rol por defecto (por ejemplo, "Cliente")
        rol_cliente = Rol.objects.get(nombre="Cliente")
        usuario.rol = rol_cliente

        if commit:
            usuario.save()
        return usuario

    def clean_password(self):
        password = self.cleaned_data.get("password")
        # Validaciones de seguridad
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(c.isdigit() for c in password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not any(c.isupper() for c in password):
            raise forms.ValidationError("La contraseña debe tener al menos una letra mayúscula.")
        if not any(c in "!@#$%^&*()_+-=[]{}|;':,.<>?/~`" for c in password):
            raise forms.ValidationError("La contraseña debe tener al menos un caracter especial.")
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar = cleaned_data.get("confirmar_password")

        if password and confirmar and password != confirmar:
            raise ValidationError("Las contraseñas no coinciden.")


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen_url', 'plataforma', 'categoria']    
