# 🎮 TiendaWeb - Proyecto Django

Link Repositorio GIT: https://github.com/dbdominguez/Django.git

## INDICE
1.-Aclaracion
2.-Proyecto
3.-Estructura del Proyecto
4.-API y Postman

# 1.- ACLARACION
Para la conexion de BD se hace uso de Instant Client Version 23.7.0.25.01 Basic Package(asegurar que la vr de python coincida con el Client), en caso de no tener el archivo (oraociei.dll) dado que decidio acceder al proyecto desde el respositorio debe descargar el packge desde la pagina:
url= https://www.oracle.com/cl/database/technologies/instant-client/winx64-64-downloads.html, Version 23.7.0.25.01 Basic Package

# ** oraociei.dll NO puede ser añadido al repositorio debido a su tamaño.

Desde el cmd utilizar: set TNS_ADMIN= \La\ruta\que\corresponda\para\dar\con\la\carpeta\Wallet

Dentro de la carpeta Wallet, en el archivo sqlnet.ora verifique la ruta del WALLET_LOCATION (debe coincidir con la ruta utilizada en el TNS_ADMIN)

Instalar:
-pip install oracledb
-pip install python-decouple
-pip install requests
-pip install djangorestframework

*Recuerda activar entorno virtual


# 2.- Proyecto
Este proyecto corresponde a una tienda de videojuegos desarrollada en Django, que debiera incluir:

- Autenticación personalizada con modelo de usuario conectado a base de datos Oracle
- Registro e inicio de sesión de usuarios (cliente/administrador)
- Administración de productos y usuarios (CRUD)
- API propia y consumo de API externa
- Interfaz moderna y responsiva con Bootstrap

# 3.- 📁 Estructura del Proyecto

TiendaWeb/
├── instantclient_23_7/
├── META-INF/
├── miapp/
│   ├── _pycache_  
│   ├── migrations                           
│   ├── static/                      # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/                   # Plantillas HTML
│   │   ├── base.html                # Plantilla base común
│   │   ├── Index.html               
│   │   ├── Registro.html            
│   │   ├── Perfil.html              
│   │   ├── PerfilAdmin.html         
│   │   ├── listar_usuarios.html    
│   │   ├── formulario_usuarios.html
│   │   ├── listar_productos.html   
│   │   ├── formulario_producto.html
│   │   └── productos_api.html
│   │   └── etc.
│   ├── _init_.py 
│   ├── admin.py 
│   ├── apps.py             
│   ├── forms.py              
│   ├── models.py
│   ├── serializers.py                        
│   ├── tests.py                     
│   ├── urls.py                      
│   └── views.py
├── proyecto/                        
├── TiendaWeb/
│   ├── _pycache_                 
│   ├── _init_.py  
│   ├── asgi.py                 
│   ├── oracle_init.py                          
│   ├── settings.py                  
│   ├── urls.py                       
│   └── wsgi.py
├── Wallet/                        
│   ├── cwallet.sso                  
│   ├── ewallet.p12
│   ├── ewallet.pem                  
│   ├── keystore.jks
│   ├── ojdbc.properties                 
│   ├── README
│   ├── sqlnet.ora                  
│   ├── tnsnames.ora                     
│   └── truststore.jks                      
├── db.sqlite3                       
├── manage.py                         
├── script_tablas.sql   
└── datos_iniciales.json      

# 4.- API y Postman

a.- Instalar Postman
b.- Nuevo (" + ")
c.- Obtener el Token de Acceso:
URL: http://127.0.0.1:8000/api/token/
Método: POST
Cuerpo (Body):
x-www-form-urlencoded

- "Key" : "Value"

{  
  "correo": "correo_de_usuario",
  "password": "contraseña"
}

#### USADO
{
  "correo": adminprueba@correo.com,
  "password": Contraseña2!
}

Si el Token es generado correctamente:
{
  "token": "tu_token_de_acceso"
}

#### EN ESTE CASO
{
  "token": d3658638e9bd0f57cb5abd362944f17ba7d3fcab
}

d.- Usar el Token de Acceso:
Método: GET o POST (dependiendo)

URL: url/api/correspondiente

Encabezados (Headers):

- "Key" : "Value"
Authorization: Token "tu_token_de_acceso"

#### EN ESTE CASO 

URL: http://127.0.0.1:8000/api/productos/ o URL: http://127.0.0.1:8000/api/categorias/


Authorization: Token d3658638e9bd0f57cb5abd362944f17ba7d3fcab







