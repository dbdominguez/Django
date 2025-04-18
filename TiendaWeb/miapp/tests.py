from django.test import TestCase, Client
from django.urls import reverse
from .models import Usuario, Producto, Categoria, Carrito, ItemCarrito, Compra

class TiendaTestCase(TestCase):

    def setUp(self):
        self.cliente = Client()
        self.usuario = Usuario.objects.create_user(username='testuser', password='testpass', rol='cliente')
        self.categoria = Categoria.objects.create(nombre='Acción')
        self.producto = Producto.objects.create(
            nombre='Juego 1',
            descripcion='Descripción del juego',
            precio=10000,
            stock=10,
            categoria=self.categoria
        )

    def test_registro_usuario(self):
        response = self.cliente.post(reverse('registro'), {
            'username': 'nuevo',
            'password1': 'Clave123@',
            'password2': 'Clave123@',
            'email': 'nuevo@correo.com',
            'rol': 'cliente',
            'direccion': 'Calle falsa 123',
        })
        self.assertEqual(response.status_code, 302)  # redirige después del registro
        self.assertTrue(Usuario.objects.filter(username='nuevo').exists())

    def test_login_usuario(self):
        response = self.cliente.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, 302)  # redirige después de login

    def test_agregar_producto_al_carrito(self):
        self.cliente.login(username='testuser', password='testpass')
        response = self.cliente.get(reverse('agregar_al_carrito', args=[self.producto.id]))
        self.assertEqual(response.status_code, 302)
        carrito = Carrito.objects.get(usuario=self.usuario, activo=True)
        self.assertTrue(ItemCarrito.objects.filter(carrito=carrito, producto=self.producto).exists())

    def test_procesar_compra(self):
        self.cliente.login(username='testuser', password='testpass')
        self.cliente.get(reverse('agregar_al_carrito', args=[self.producto.id]))
        response = self.cliente.post(reverse('procesar_compra'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Compra.objects.filter(usuario=self.usuario).exists())
# Create your tests here.
