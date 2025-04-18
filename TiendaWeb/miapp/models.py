from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255)  # Path a la imagen
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    desarrollador = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return self.usuario.username

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    tipo_documento = models.CharField(max_length=20, choices=[('boleta', 'Boleta'), ('factura', 'Factura')])
    metodo_entrega = models.CharField(max_length=20, choices=[('envio', 'Envío a domicilio'), ('retiro', 'Retiro en local')])
    
    def __str__(self):
        return f'Orden {self.id} - {self.usuario.username}'
    
    @property
    def get_total(self):
        items = self.ordenitem_set.all()
        total = sum([item.get_total for item in items])
        return total

class OrdenItem(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        return self.juego.precio * self.cantidad

class Valoracion(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('juego', 'usuario')
    
    def __str__(self):
        return f'{self.usuario.username} - {self.juego.nombre} - {self.puntuacion}'
