from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# ROL Tabla
class Rol(models.Model):
    class Meta:
        db_table = 'MAIN_ROL'
    id_rol = models.AutoField(primary_key=True, db_column='ID_ROL')
    nombre = models.CharField(max_length=50, db_column='NOMBRE')

    def __str__(self):
        return self.nombre


#Inicio Sesion Autenticacion
class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo es obligatorio')
        correo = self.normalize_email(correo)
        usuario = self.model(correo=correo, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Aquí asignamos el rol de administrador
        from miapp.models import Rol  # Importar el modelo Rol si no está en el mismo archivo
        rol_admin = Rol.objects.get(nombre='Administrador')  # Asegúrate de que este rol exista
        extra_fields.setdefault('rol', rol_admin)

        return self.create_user(correo, password, **extra_fields)

#USUARIO
class Usuario(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'USUARIO'

    id_usuario = models.AutoField(primary_key=True, db_column='ID_USUARIO')
    nombre = models.CharField(max_length=100, db_column='NOMBRE', null=True)
    apellido = models.CharField(max_length=100, db_column='APELLIDO', null=True)
    rol = models.ForeignKey('Rol', on_delete=models.PROTECT, db_column='ID_ROL')
    correo = models.EmailField(unique=True, db_column='CORREO')
    direccion = models.CharField(max_length=255, db_column='DIRECCION', null=True, blank=True)
    telefono = models.CharField(max_length=20, db_column='TELEFONO', null=True, blank=True)
    password = models.CharField(max_length=255, db_column='PASSWORD')
    is_active = models.BooleanField(default=True, db_column='ACTIVO')
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    objects = UsuarioManager()

    def __str__(self):
        return self.correo


# CATEGORIA Tabla
class Categoria(models.Model):
    class Meta:
        db_table = 'CATEGORIA'
    id_categoria = models.AutoField(primary_key=True, db_column='ID_CATEGORIA')
    nombre = models.CharField(max_length=50, db_column='NOMBRE')

    def __str__(self):
        return self.nombre

# PLATAFORMA Tabla
class Plataforma(models.Model):
    class Meta:
        db_table = 'PLATAFORMA'
    id_categoria = models.AutoField(primary_key=True, db_column='ID_PLATAFORMA')
    nombre = models.CharField(max_length=50, db_column='NOMBRE')

    def __str__(self):
        return self.nombre

# PRODUCTO tabla
class Producto(models.Model):
    class Meta:
        db_table = 'PRODUCTO'
    id_producto = models.AutoField(primary_key=True, db_column='ID_PRODUCTO')
    nombre = models.CharField(max_length=100, db_column='NOMBRE')
    descripcion = models.TextField(db_column='DESCRIPCION', null=True, blank=True)
    precio = models.DecimalField(db_column='PRECIO')
    stock = models.IntegerField(default=0, db_column='STOCK')
    imagen_url = models.CharField(max_length=255, db_column='IMAGEN_URL', null=True, blank=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, db_column='ID_PLATAFORMA')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='ID_CATEGORIA')


#CARRITO TABLA
class Carrito(models.Model):
    class Meta:
        db_table = 'CARRITO'
    id_carrito = models.AutoField(primary_key=True, db_column='ID_CARRITO')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='ID_USUARIO')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='ID_PRODUCTO')
    cantidad = models.PositiveIntegerField(db_column='CANTIDAD')


#COMPRA TABLA
class Compra(models.Model):
    class Meta:
        db_table = 'COMPRA'
    id_compra = models.AutoField(primary_key=True, db_column='ID_COMPRA')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='ID_USUARIO')
    fecha = models.DateTimeField(auto_now_add=True, db_column='FECHA')
    total = models.DecimalField(max_digits=10, decimal_places=2, db_column='TOTAL')
    estado = models.CharField(max_length=50, db_column='ESTADO')


#DETALLECOMPRA Tabla
class DetalleCompra(models.Model):
    class Meta:
        db_table = 'DETALLE_COMPRA'
    id_detalle = models.AutoField(primary_key=True, db_column='ID_DETALLE')
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, db_column='ID_COMPRA')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='ID_PRODUCTO')
    cantidad = models.PositiveIntegerField(db_column='CANTIDAD')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, db_column='PRECIO_UNITARIO')

