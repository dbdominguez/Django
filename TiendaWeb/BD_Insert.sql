--Datos
--ROL
INSERT INTO MAIN_ROL (ID_ROL, NOMBRE) VALUES (1, 'Administrador');
INSERT INTO MAIN_ROL (ID_ROL, NOMBRE) VALUES (2, 'Cliente');

--USUARIO
INSERT INTO USUARIO (
  ID_USUARIO, NOMBRE, APELLIDO, ROL, CORREO, DIRECCION, TELEFONO, CLAVE,
  IS_ACTIVE, IS_STAFF, IS_SUPERUSER, LAST_LOGIN
) VALUES 
(1, 'Juan', 'Padilla', 2, 'clienteprueba@correo.com', 'Calle Valparaiso 810', '123456789',
 'pbkdf2_sha256$1000000$T6F6VAyp3PQz6byxhzgpaR$BakaCqdfTnYxlliWgc866q4aIpQxEevQAP53nTFo39E=',
 1, 0, 0, TO_TIMESTAMP('2025-04-22 01:42:38.500', 'YYYY-MM-DD HH24:MI:SS.FF'));

INSERT INTO USUARIO (
  ID_USUARIO, NOMBRE, APELLIDO, ROL, CORREO, DIRECCION, TELEFONO, CLAVE,
  IS_ACTIVE, IS_STAFF, IS_SUPERUSER, LAST_LOGIN
) VALUES 
(3, 'Raul', 'Perez', 1, 'adminprueba@correo.com', '', '',
 'pbkdf2_sha256$1000000$U9c2LBBWIhkk59Tv8cGy4k$aymku3mKVcjpQAxgHptun1MJZesjdf+jB/MPKE2d33c=',
 1, 1, 1, TO_TIMESTAMP('2025-05-05 18:30:14.122', 'YYYY-MM-DD HH24:MI:SS.FF'));

--CATEGORIAS
INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES (1, 'Survival Horror');
INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES (2, 'Estrategia');
INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES (3, 'Deporte');
INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES (4, 'Simuladores');
INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES (5, 'Visual Novel');
INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES (6, 'RPG');
INSERT INTO CATEGORIA (ID_CATEGORIA, NOMBRE) VALUES (7, 'Arcade Clasicos');

--PLATAFORMA
INSERT INTO PLATAFORMA (ID_PLATAFORMA, NOMBRE) VALUES (1, 'PC (STEAM)');
INSERT INTO PLATAFORMA (ID_PLATAFORMA, NOMBRE) VALUES (2, 'Nintendo Switch');
INSERT INTO PLATAFORMA (ID_PLATAFORMA, NOMBRE) VALUES (3, 'PlayStation 4');
INSERT INTO PLATAFORMA (ID_PLATAFORMA, NOMBRE) VALUES (4, 'Xbox 360');

--PRODUCTO
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (5, 'Silent Hill 2: Remake', 'Vive la pesadilla en el remake del clásico de terror psicológico Silent Hill 2. Acompaña a James Sunderland en su aterradora búsqueda por su esposa fallecida, enfrentándote a criaturas deformadas y resolviendo enigmas en un pueblo oscuro y lleno de secretos.', 46990.00, 44, '/static/core/Imagenes/caratula/sh2r.png', 4, 1);
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (6, 'Resident Evil 2: Remake', 'Revive el horror de Resident Evil 2 en este remake totalmente renovado. Acompaña a Leon S. Kennedy y Claire Redfield en su lucha por sobrevivir en Raccoon City, enfrentándose a zombis, monstruos y otros horrores mientras exploran un entorno peligroso y lleno de tensión.', 21990.00, 25, '/static/core/Imagenes/caratula/re2r.png', 3, 1);

INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (7, 'Age of Empires II: Definitive Edition', '¡Revive la historia y construye tu imperio! Este juego de estrategia en tiempo real te lleva a través de las épocas, permitiéndote liderar civilizaciones icónicas, librar batallas épicas y tomar decisiones que cambiarán el curso de la historia. Con campañas emocionantes y una jugabilidad profunda, es perfecto para los amantes de la estrategia. ¡El destino de tu imperio está en tus manos!', 15990.00, 34, '/static/core/Imagenes/caratula/age2.png', 1, 2);
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (8, 'Civilization VI', '¡Da forma al mundo como un verdadero líder! Este aclamado juego de estrategia por turnos te permite construir y expandir tu civilización desde los albores de la humanidad hasta la era moderna. Toma decisiones cruciales, negocia con líderes históricos y asegura tu lugar en la historia. Con mapas dinámicos y un sinfín de posibilidades, cada partida es una experiencia única. ¡El destino de tu civilización está en tus manos!', 5990.00, 32, '/static/core/Imagenes/caratula/civVI.png', 1, 2);

INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (9, 'Mario Strikers: Battle League', '¡El fútbol más alocado regresa con Mario y sus amigos! Compite en intensos partidos de 5 contra 5 donde todo vale, usando movimientos especiales y equipamiento para personalizar tu estilo de juego. Juega en solitario, en línea o con amigos en este caótico y divertido arcade deportivo.', 44990.00, 15, '/static/core/Imagenes/caratula/MSBLF.png', 2, 3);
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (10, 'NBA 2K24', 'Vive la emoción del baloncesto con la entrega más realista de la saga NBA 2K. Disfruta de modos como Mi Carrera, Mi Equipo y la WNBA, con gráficos impresionantes y mecánicas de juego mejoradas. Con estrellas de la NBA, personalización profunda y experiencias competitivas en línea, NBA 2K24 es el juego definitivo para los fanáticos del básquetbol.', 45990.00, 32, '/static/core/Imagenes/caratula/NBA2k24.png', 2, 3);

INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (11, 'Stardew Valley', 'Crea y gestiona tu propia granja en este relajante simulador de vida. Siembra, cultiva, pesca y forja relaciones con los habitantes del pueblo mientras exploras minas, enfrentas monstruos y vives una vida tranquila en el campo.', 7500.00, 36, '/static/core/Imagenes/caratula/SV.png', 3, 4);
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (12, 'Microsoft Flight Simulator 2024', 'Experimenta el realismo definitivo en simulación de vuelo con Microsoft Flight Simulator 2024. Pilota una amplia variedad de aeronaves en un mundo hiperrealista con condiciones climáticas dinámicas, tráfico aéreo en tiempo real y misiones emocionantes', 51990.00, 63, '/static/core/Imagenes/caratula/MFS2024.png', 3, 4);

INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (13, 'Ace Attorney Trilogy: Apollo Justice', 'Únete al abogado Apollo Justice y su mentor, el legendario Phoenix Wright, en esta colección de 3 juegos. Este título incluye 16 episodios (incluidos los que antes solo se conseguían como DLC) y está disponible en inglés, francés, alemán, japonés, coreano y chino tradicional y simplificado.', 49990.00, 12, '/static/core/Imagenes/caratula/AAT.png', 3, 5);
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (14, 'Danganronpa V3: Killing Harmony', 'Un elenco nuevo de 16 personajes está atrapado en una escuela. Algunos matarán, otros morirán y otros recibirán un castigo. Dales una nueva mirada a los riesgos y la investigación dinámica mientras tratas de resolver casos retorcidos y condenar a muerte a tus nuevos amigos.', 14990.00, 56, '/static/core/Imagenes/caratula/danganv3.png', 4, 5);

INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (15, 'Kingdom Hearts III + Re Mind (DLC)', 'Embárcate en una épica aventura junto a Sora, Donald y Goofy en este emocionante RPG de acción. Explora mundos inspirados en Disney y Pixar, lucha contra la oscuridad con el poder de la Llave Espada y descubre el desenlace de la saga de Xehanort.', 42990.00, 14, '/static/core/Imagenes/caratula/kh3.png', 3, 6);
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (16, 'Persona 5', 'Sumérgete en el mundo de los "Phantom Thieves" en este aclamado JRPG. Vive la vida de un estudiante de secundaria en Tokio, forma relaciones, mejora tus habilidades y lucha en un mundo surrealista para cambiar los corazones de los corruptos. Con una jugabilidad que combina exploración, gestión del tiempo y combates por turnos, Persona 5 ofrece una experiencia única y emocionante.', 19990.00, 14, '/static/core/Imagenes/caratula/per5.png', 3, 6);

INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (17, 'Pac-man Museum', 'Juega los 14 títulos legendarios, como el clásico PAC-MAN y PAC-LAND, así como también el recién incorporado PAC-IN-TIME y PAC-MAN 256. Ya sea si prefieres la acción de desplazamiento lateral del PAC-MAN original o el género de los rompecabezas, ¡esta colección tiene algo para todos!', 32990.00, 15, '/static/core/Imagenes/caratula/PCMus.png', 2, 7);
INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, DESCRIPCION, PRECIO, STOCK, ID_CATEGORIA, ID_PLATAFORMA) VALUES (18, 'Virtua fighter 5', '¡El clásico de lucha que marcó un antes y un después en los videojuegos! Este título, desarrollado por Sega, ofrece combates intensos con un elenco diverso de personajes, cada uno con estilos de lucha únicos. Con gráficos impresionantes y mecánicas de juego refinadas, es una experiencia imprescindible para los amantes de los juegos de pelea. ¡Domina el arte del combate y demuestra tus habilidades en el ring virtual!', 19990.00, 17, '/static/core/Imagenes/caratula/vf5.png', 4, 7);


COMMIT;
