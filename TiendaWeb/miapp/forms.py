from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

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
