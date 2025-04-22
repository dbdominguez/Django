# 🎮 TiendaWeb - Proyecto Django

## ACLARACION

Durante el desarrollo la conexion a base de datos Oracle presento multiples problemes, aunque se logro hacer conexion una pc en especifico faltaron ensayos
para comprobar si se puede hacer conexion desde un equipo ajeno.

Para la conexion se incluyo dentro del proyecto la carpeta con el Instant Client Version 23.7.0.25.01 Basic Package(asegurar que la vr de python sea la misma que del cliente -x64 o x32-) sin embargo se requiere que el usuario consiga el Instant Client desde la pagina Oracle debido a que un archivo (oraociei.dll) no puede ser añadido al repositorio debido a su tamaño.

Desde el cmd utilizar: set TNS_ADMIN= \La\ruta\que\corresponda\para\dar\con\la\carpeta\Wallet"

Dentro de la carpeta Wallet, en el archivo sqlnet.ora verifique la ruta del WALLET_LOCATION (debe coincidir con la ruta utilizada en el TNS_ADMIN)

Asegurese de tener instalado:
-pip install oracledb
-pip install python-decouple
-pip install requests
-pip install djangorestframework

*Recuerda activar entorno virtual

### NOTA: Existe un error de Oracle "ORA-01804" asociado con la falta de archivos relacionados con la zona horaria que puede llegar a ocurrir, la version utilizada del Instant Client ya no trae dicho archivo. Se desconoce como solucionar dicho error a no ser que en el equipo hayan existido con anterioridad los archivos que se solicitan.


#### Proyecto
Este proyecto corresponde a una tienda de videojuegos desarrollada en Django, que debiera incluir:

- Autenticación personalizada con modelo de usuario conectado a base de datos Oracle
- Registro e inicio de sesión de usuarios (cliente/administrador)
- Administración de productos y usuarios (CRUD)
- API propia y consumo de API externa
- Interfaz moderna y responsiva con Bootstrap

##### 📁 Estructura del Proyecto

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
└── README.md                         # Documentación del proyecto






