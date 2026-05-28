



TRABAJO ESPECIAL

SUBMÓDULO:
IMPLEMENTA BASE DE DATOS RELACIONALES EN UN SISTEMA DE INFORMACIÓN 

PROFESOR:
JOSE CHRISTIAN ROMERO HERNANDEZ

GRUPO: 4 AVPG

NOMBRE DEL TRABAJO:  
Proyecto Final 


ALUMNOS:
Camacho Molinares Valentina 
Flores Bravo Stephanie Naomi 
Ramos Camargo Kharly Alejandra 
Rubio Camacho Omar Alejandro 
Torres Bon Mario Alfredo 
Velarde Quintero Natalia
	
	




                                       Tijuana, B.C. a 28 de mayo de 2026
 
ÍNDICE
Portada
Introducción
Objetivo del Proyecto
Instalación del Proyecto
Estructura del Proyecto
     5.1 Carpeta perfumería
asgi.py
settings.py
urls.py
wsgi.py
    5.2 Carpeta perfumes
admin.py
apps.py
models.py
tests.py
urls.py
views.py
     5.3 Carpeta migrations
0001_initial.py
     5.4 Carpeta templates
detalle.html 
lista.html
carrito.html

Explicación de models.py
Relaciones de Base de Datos
Explicación de admin.py
Explicación de views.py
Explicación de urls.py
Funcionamiento CRUD
Diseño de la Base de Datos
Conclusiones

INTRODUCCIÓN 
El presente proyecto consiste en el desarrollo de un sistema web para la gestión y visualización de una perfumería en línea, denominada Perfumería Élite, construido utilizando el framework Django de Python como tecnología principal. El sistema permite administrar un catálogo completo de fragancias organizadas en tres categorías principales: perfumes de diseñador, perfumes árabes y perfumes de nicho, abarcando las marcas más reconocidas a nivel mundial como Chanel, Dior, Tom Ford, Amouage, Creed y Maison Francis Kurkdjian, entre muchas otras.
El sistema fue desarrollado con el objetivo de aplicar los conocimientos adquiridos en el curso sobre bases de datos relacionales y desarrollo web, implementando los conceptos fundamentales de modelado de datos mediante el uso del ORM de Django. La base de datos del proyecto contempla relaciones de uno a muchos, como la existente entre una marca y sus perfumes, así como relaciones de muchos a muchos, como la que existe entre los perfumes y las colecciones temáticas, y la que se establece entre los usuarios y los perfumes a través del carrito de compras.
La estructura del proyecto comprende seis modelos principales: Marca, Perfume, Colección, Reseña, Carrito y CarritoItem, cada uno diseñado para cubrir una necesidad específica dentro del sistema. El modelo de Perfume concentra la información central del catálogo, incluyendo nombre, precio, volumen en mililitros, género, categoría, notas olfativas, stock disponible e imagen de referencia. Las colecciones permiten agrupar perfumes bajo temáticas especiales como colecciones de temporada o selecciones por género, mientras que las reseñas permiten registrar la opinión y calificación de los clientes sobre cada fragancia.
La interfaz del sistema cuenta con un panel de administración robusto, desarrollado sobre el administrador nativo de Django, en el cual es posible realizar operaciones completas de alta, consulta, modificación y baja de registros para cada uno de los modelos. Adicionalmente, el sistema cuenta con una interfaz pública de visualización del catálogo, diseñada con un estilo elegante y oscuro acorde a la identidad visual de una perfumería de lujo, donde los usuarios pueden explorar el catálogo completo, consultar el detalle de cada fragancia y visualizar las reseñas de otros clientes.
El proyecto fue desarrollado en su totalidad utilizando Python 3.13, Django 5.2, SQLite como motor de base de datos y Visual Studio Code como entorno de desarrollo, siguiendo buenas prácticas de organización de código y estructura de proyectos web.


OBJETIVO DEL PROYECTO 
El objetivo principal del proyecto PARFUMS es desarrollar una aplicación web funcional utilizando el lenguaje de programación Python y el framework Django, aplicando los conocimientos de programación, desarrollo web y bases de datos relacionales aprendidos durante el curso.
El sistema fue diseñado para administrar una tienda de perfumes mediante una plataforma que permita registrar, visualizar, modificar y eliminar información relacionada con perfumes, marcas, colecciones, reseñas y carritos de compra.
A nivel de programación, el proyecto tiene como finalidad implementar correctamente la arquitectura MTV (Model - Template - View) de Django, permitiendo la interacción entre:
los modelos de base de datos,
las vistas del sistema,
las URLs,
y las interfaces visuales creadas con templates HTML.
Además, el proyecto busca demostrar el funcionamiento de relaciones dentro de una base de datos relacional, implementando:
relaciones de Uno a Muchos,
y relaciones de Muchos a Muchos,
utilizando Django ORM para conectar los diferentes modelos del sistema.
También se implementaron operaciones CRUD (Crear, Leer, Actualizar y Eliminar) desde el panel administrativo de Django, permitiendo gestionar toda la información de manera dinámica y organizada.
Finalmente, el proyecto tiene como propósito fortalecer habilidades de programación como:
organización de código,
estructura de proyectos,
manejo de rutas,
uso de clases y modelos,
manipulación de datos,
manejo de imágenes con Pillow,
y control de versiones mediante Git y GitHub.


INSTALACIÓN DEL PROYECTO 
Para ejecutar correctamente el proyecto PARFUMS fue necesario instalar y configurar diferentes herramientas y dependencias de programación.
Primero se creó un entorno virtual utilizando Python para mantener organizadas las librerías del proyecto y evitar conflictos con otros programas instalados en la computadora.
python -m venv venv
Después se activó el entorno virtual para comenzar a trabajar dentro del proyecto.
venv\Scripts\activate
Luego se instaló Django versión 5.2, el framework principal utilizado para desarrollar toda la aplicación web.
pip install django==5.2
También se instaló la librería Pillow, utilizada para el manejo y almacenamiento de imágenes dentro del sistema, especialmente para las imágenes de perfumes.
pip install pillow
Posteriormente se clonó el repositorio del proyecto desde GitHub utilizando Git.
git clone https://github.com/Alxjandrz/PARFUMS.git
Después se ingresó a la carpeta principal del proyecto.
cd PARFUMS
Para mantener el proyecto actualizado se utilizaron los comandos:
git fetch
git pull
Finalmente se abrió el proyecto en Visual Studio Code para continuar con el desarrollo y programación del sistema.
code .
Una vez configurado todo el entorno, se ejecutaron las migraciones de la base de datos y se inició el servidor de Django.
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
ESTRUCTURA 
Carpeta perfumeria
asgi.py
El archivo asgi.py forma parte de la configuración principal del proyecto Django y permite que la aplicación pueda comunicarse correctamente con el servidor web.
Su función principal es preparar y ejecutar el proyecto utilizando ASGI, una tecnología que permite manejar múltiples conexiones y procesos de manera más eficiente.
En este archivo también se indica cuál es la configuración principal del proyecto, utilizando el archivo settings.py de la carpeta Perfumeria.
Finalmente, se crea la aplicación principal de Django para que el servidor pueda ejecutar correctamente el sistema web.


settings.py
El archivo settings.py es uno de los archivos más importantes del proyecto, ya que contiene toda la configuración principal de Django y controla el funcionamiento general de la aplicación.
En este archivo se define la ruta principal del proyecto mediante BASE_DIR, lo que permite ubicar correctamente carpetas y archivos dentro del sistema.
También se configura la clave secreta del proyecto, utilizada por Django para proporcionar seguridad interna en la aplicación.
La opción DEBUG se encuentra activada en True, lo que permite visualizar errores y facilitar el desarrollo y pruebas del proyecto mientras se programa.
Dentro de INSTALLED_APPS se registran todas las aplicaciones que utilizará el sistema. Además de las aplicaciones propias de Django, se agregó la aplicación perfumes, que contiene toda la lógica principal del proyecto.
La sección MIDDLEWARE contiene herramientas internas de Django que ayudan a manejar:
seguridad,
sesiones,
autenticación,
mensajes,
y protección de formularios.
ROOT_URLCONF indica cuál es el archivo principal encargado de manejar las URLs del proyecto.
La configuración TEMPLATES permite utilizar archivos HTML para crear la interfaz visual del sistema y conectar las vistas con las plantillas.
WSGI_APPLICATION prepara la aplicación para ejecutarse en un servidor web.
En DATABASES se configura la base de datos del proyecto. En este caso se utiliza SQLite, una base de datos ligera que se almacena en un archivo llamado db.sqlite3.
La sección AUTH_PASSWORD_VALIDATORS contiene validaciones de seguridad para las contraseñas de los usuarios, ayudando a proteger el sistema.
También se configura el idioma, la zona horaria y las opciones de internacionalización del proyecto.
STATIC_URL permite manejar archivos estáticos como: 
CSS,
JavaScript,
imágenes,
y estilos visuales.
DEFAULT_AUTO_FIELD configura el tipo de identificador automático utilizado por Django en los modelos.
Además, se configuró un modelo de usuario personalizado mediante:
AUTH_USER_MODEL
lo que permite utilizar el modelo User creado dentro de la aplicación perfumes.
Finalmente, se configuró el manejo de imágenes mediante MEDIA_URL y MEDIA_ROOT, permitiendo almacenar y mostrar imágenes de perfumes dentro del sistema web.


urls.py
El archivo urls.py se encarga de manejar las rutas principales del proyecto Django y conectar las diferentes partes de la aplicación.
En este archivo se importan herramientas necesarias para trabajar con:
rutas
configuración del proyecto
archivos multimedia
La línea:
admin.site.urls
permite acceder al panel administrativo de Django mediante la ruta /admin/.
También se incluye la aplicación perfumes utilizando include(), lo que permite conectar todas las URLs creadas dentro de esa aplicación.
De esta forma, cuando un usuario entra a la ruta /perfumes/, Django redirige automáticamente a las vistas correspondientes de la aplicación perfumes.
Además, se configuró el manejo de archivos multimedia utilizando static(), lo que permite mostrar correctamente las imágenes de perfumes almacenadas dentro de la carpeta media.
Gracias a este archivo, el sistema puede conectar:
las URLs
las vistas
los modelos
las interfaces HTML
permitiendo el correcto funcionamiento de toda la aplicación web.


wsgi.py


El archivo wsgi.py forma parte de la configuración principal del proyecto Django y se encarga de permitir la comunicación entre el servidor web y la aplicación.


Su función principal es preparar el proyecto para que pueda ejecutarse correctamente en servidores web compatibles con WSGI.


En este archivo se importa la configuración principal del proyecto utilizando el archivo settings.py de la carpeta Perfumeria.


También se crea la aplicación principal de Django, la cual será utilizada por el servidor para ejecutar el sistema web.


Este archivo es importante porque permite que la aplicación pueda funcionar correctamente cuando se despliega en un entorno de producción o en un servidor web.








Carpeta perfumes 

admin.py
El archivo models.py es uno de los más importantes del proyecto, ya que contiene todos los modelos de la base de datos. Cada modelo representa una tabla distinta dentro del sistema y permite almacenar información relacionada con la perfumería.
Primero se importan las herramientas necesarias de Django y la librería uuid, utilizada para generar identificadores únicos para cada registro.
El modelo User representa a los usuarios del sistema. Este modelo hereda de AbstractUser, lo que permite utilizar el sistema de autenticación de Django y agregar nuevas características personalizadas. En este caso, se añadió el campo is_seller para identificar si el usuario es vendedor. Además, se utiliza UUID como identificador principal para mejorar la seguridad del sistema.
El modelo Marca representa las marcas de perfumes. Cada marca almacena:
nombre
país de origen
Este modelo tiene una relación de Uno a Muchos con el modelo Perfume, lo que significa que una marca puede tener muchos perfumes registrados.
El modelo Perfume representa los productos principales del sistema. Aquí se almacena información como:
nombre
marca
precio
stock
mililitros
género
categoría
notas olfativas
imágenes
También se agregaron opciones de selección para género y categoría, facilitando el ingreso de datos desde el panel administrativo.
Este modelo tiene varias relaciones importantes:
pertenece a una marca
puede tener muchas reseñas
puede estar en muchas colecciones
puede agregarse a muchos carritos
Además, se implementó ImageField para permitir subir imágenes de perfumes al sistema.
El modelo Coleccion sirve para agrupar perfumes dentro de diferentes categorías o temporadas. Este modelo utiliza una relación de Muchos a Muchos con Perfume, lo que significa que:
una colección puede contener muchos perfumes
un perfume puede pertenecer a muchas colecciones
Esta es una de las relaciones más importantes del proyecto porque demuestra el uso de relaciones complejas dentro de bases de datos relacionales.
El modelo Resena permite almacenar opiniones y calificaciones de clientes sobre perfumes. Cada reseña contiene:
nombre del cliente
calificación
comentario
fecha
Este modelo tiene una relación de Uno a Muchos con Perfume, ya que un perfume puede tener muchas reseñas.
El modelo Carrito representa el carrito de compras de cada usuario. Cada carrito pertenece a un usuario específico y almacena la fecha de creación.
También se implementó una propiedad llamada total, la cual calcula automáticamente el precio total de todos los productos agregados al carrito.
El modelo CarritoItem funciona como una tabla intermedia entre Carrito y Perfume. Este modelo permite almacenar:
el perfume agregada
la cantidad seleccionada
el subtotal de la compra
Además, se implementó una restricción para evitar que un mismo perfume se repita varias veces dentro del mismo carrito.















apps.py
El archivo apps.py se encarga de configurar la aplicación perfumes dentro del proyecto Django.
En este archivo se define la clase PerfumesConfig, la cual representa la configuración principal de la aplicación.
La línea:
default_auto_field
configura el tipo de identificador automático que utilizarán los modelos del sistema.
Por otro lado, la línea:
name = ‘perfumes’
indica el nombre oficial de la aplicación registrada dentro del proyecto Django.
Este archivo ayuda a que Django reconozca correctamente la aplicación perfumes y pueda integrarla con el resto del sistema.

models.py
El archivo models.py es uno de los más importantes del proyecto, ya que contiene todos los modelos de la base de datos. Cada modelo representa una tabla distinta dentro del sistema y permite almacenar información relacionada con la perfumería.
Primero se importan las herramientas necesarias de Django y la librería uuid, utilizada para generar identificadores únicos para cada registro.
El modelo User representa a los usuarios del sistema. Este modelo hereda de AbstractUser, lo que permite utilizar el sistema de autenticación de Django y agregar nuevas características personalizadas. En este caso, se añadió el campo is_seller para identificar si el usuario es vendedor. Además, se utiliza UUID como identificador principal para mejorar la seguridad del sistema.
El modelo Marca representa las marcas de perfumes. Cada marca almacena:
nombre
país de origen
Este modelo tiene una relación de Uno a Muchos con el modelo Perfume, lo que significa que una marca puede tener muchos perfumes registrados.
El modelo Perfume representa los productos principales del sistema. Aquí se almacena información como:
nombre
marca
precio
stock
mililitros
género
categoría
notas olfativas
imágenes
También se agregaron opciones de selección para género y categoría, facilitando el ingreso de datos desde el panel administrativo.
Este modelo tiene varias relaciones importantes:
pertenece a una marca
puede tener muchas reseñas
puede estar en muchas colecciones
puede agregarse a muchos carritos
Además, se implementó ImageField para permitir subir imágenes de perfumes al sistema.
El modelo Coleccion sirve para agrupar perfumes dentro de diferentes categorías o temporadas. Este modelo utiliza una relación de Muchos a Muchos con Perfume, lo que significa que:
una colección puede contener muchos perfumes
un perfume puede pertenecer a muchas colecciones
Esta es una de las relaciones más importantes del proyecto porque demuestra el uso de relaciones complejas dentro de bases de datos relacionales.
El modelo Resena permite almacenar opiniones y calificaciones de clientes sobre perfumes. Cada reseña contiene:
nombre del cliente
calificación
comentario
fecha
Este modelo tiene una relación de Uno a Muchos con Perfume, ya que un perfume puede tener muchas reseñas.
El modelo Carrito representa el carrito de compras de cada usuario. Cada carrito pertenece a un usuario específico y almacena la fecha de creación.
También se implementó una propiedad llamada total, la cual calcula automáticamente el precio total de todos los productos agregados al carrito.
El modelo CarritoItem funciona como una tabla intermedia entre Carrito y Perfume. Este modelo permite almacenar:
el perfume agregado
la cantidad seleccionada
el subtotal de la compra
Además, se implementó una restricción para evitar que un mismo perfume se repita varias veces dentro del mismo carrito.
En general, este archivo es el encargado de estructurar toda la base de datos del proyecto y definir las relaciones entre los diferentes modelos del sistema

tests.py
El archivo tests.py se utiliza para realizar pruebas dentro del proyecto Django.
Su función principal es verificar que las diferentes partes del sistema funcionen correctamente, evitando errores durante el desarrollo de la aplicación.
En este caso, el archivo únicamente importa TestCase desde Django, una herramienta utilizada para crear pruebas automáticas.
Actualmente el archivo no contiene pruebas programadas, por lo que solamente aparece el comentario:
Create your tests here.
Esto indica que el archivo está preparado para agregar pruebas en el futuro, como:
pruebas de modelos
pruebas de vistas
validaciones de formularios 
funcionamiento de URLs
Aunque en este proyecto no se implementaron pruebas automáticas, el archivo forma parte de la estructura estándar de Django y permite expandir el sistema posteriormente.

urls.py
El archivo urls.py de la aplicación perfumes se encarga de definir las rutas internas del sistema y conectar las URLs con las views correspondientes.
Primero se importan:
path, utilizado para crear rutas
views, donde se encuentran las funciones que controlan la lógica de la aplicación
Dentro de urlpatterns se definen las rutas principales del sistema.
La primera ruta:
‘’
representa la página principal de la aplicación perfumes. Esta ruta está conectada con la view lista_perfumes, la cual se encarga de mostrar todos los perfumes registrados en el sistema.
La segunda ruta:
‘int:pk/’
permite acceder al detalle individual de cada perfume utilizando su identificador.
Esta ruta se conecta con la view detalle_perfume, encargada de mostrar la información específica de un perfume seleccionado.
El parámetro pk representa la clave primaria del perfume y permite identificar qué registro debe mostrarse.
Gracias a este archivo, las URLs pueden comunicarse correctamente con las views para mostrar información dinámica dentro de la aplicación web.

views.py
El archivo views.py contiene la lógica principal de la aplicación y se encarga de conectar los modelos con los templates para mostrar información al usuario.
Primero se importan las herramientas necesarias de Django, como:
render, utilizada para mostrar páginas HTML
get_object_or_404, utilizada para buscar registros en la base de datos y mostrar un error si no existen
También se importan los modelos:
Perfume
Coleccion
Resena
La función lista_perfumes se encarga de mostrar todos los perfumes organizados por categorías.
Dentro de esta función se realizan consultas a la base de datos utilizando:
Perfume.objects.filter()
Estas consultas permiten separar los perfumes en:
diseñador
árabes
nicho
Después, toda esta información se envía al template lista.html utilizando render(), permitiendo mostrar los perfumes en la interfaz visual del sistema.
La función detalle_perfume se encarga de mostrar la información específica de un perfume seleccionado.
Primero se utiliza get_object_or_404 para buscar el perfume mediante su identificador. Si el perfume no existe, Django mostrará automáticamente un error 404.
Luego se obtienen:
las reseñas relacionadas con el perfume
las colecciones a las que pertenece
Las reseñas se ordenan por fecha para mostrar primero las más recientes.
Finalmente, toda esta información se envía al template detalle.html para mostrar:
información del perfume
reseñas
colecciones relacionadas
Gracias a este archivo, las views pueden comunicarse con:
los modelos
las URLs
los templates
permitiendo que la aplicación funcione dinámicamente y muestre información actualizada al usuario











Carpeta migrations
0001_initial.py
El archivo 0001_initial.py corresponde a la primera migración creada por Django para el proyecto.
Las migraciones son archivos que permiten crear y modificar automáticamente la estructura de la base de datos a partir de los modelos definidos en models.py.
Este archivo contiene todas las instrucciones necesarias para construir las tablas principales del sistema dentro de la base de datos.
Primero se importan herramientas necesarias de Django para trabajar con:
modelos
migraciones
relaciones
validaciones
identificadores UUID
La clase Migration representa la migración principal del proyecto y contiene todas las operaciones que Django ejecutará en la base de datos.
Dentro de dependencies se establece la dependencia con el sistema de autenticación de Django, permitiendo utilizar usuarios personalizados.
En operations se crean todos los modelos principales del sistema.
El modelo Marca crea la tabla encargada de almacenar:
nombre de la marca
país de origen
El modelo User crea la tabla de usuarios personalizada del sistema, incluyendo:
nombre de usuario
correo electrónico
contraseña
permisos
tipo de vendedor
El modelo Carrito crea la tabla para almacenar los carritos de compra relacionados con los usuarios.
El modelo Perfume crea la tabla principal de perfumes, donde se almacenan datos como:
nombre
precio
género
categoría
stock
descripción
imagen
marca relacionada
El modelo Coleccion crea la tabla para agrupar perfumes mediante una relación de Muchos a Muchos.
El modelo CarritoItem crea una tabla intermedia que conecta:
carritos
perfumes
permitiendo almacenar la cantidad de productos agregados al carrito.
Además, se implementa una restricción para evitar perfumes repetidos dentro del mismo carrito.
El modelo Resena crea la tabla encargada de almacenar:
clientes
comentarios
calificaciones
fechas
perfumes relacionados
En general, este archivo es el encargado de construir toda la estructura inicial de la base de datos del proyecto y establecer las relaciones entre los diferentes modelos del sistema
Carpeta templates

detalle.html
El archivo detalle.html corresponde al template encargado de mostrar la información detallada de cada perfume dentro de la aplicación web.
Este archivo utiliza HTML, CSS y el sistema de templates de Django para crear una interfaz visual elegante y dinámica.
En la parte inicial del documento se configura la estructura básica de la página, incluyendo:
idioma
codificación de caracteres
adaptación para dispositivos móviles
título dinámico utilizando el nombre del perfume
También se importan fuentes externas desde Google Fonts para mejorar el diseño visual de la página.
Dentro de la etiqueta style se encuentra todo el diseño CSS del template. Aquí se personalizan:
colores
tamaños
tipografías
espacios
diseño responsive
animaciones visuales
El diseño utiliza una apariencia moderna y elegante con colores oscuros y detalles dorados para representar una tienda de perfumes de lujo.
La clase detalle organiza todo el contenido principal de la página.
La sección volver crea un enlace que permite regresar al catálogo principal de perfumes.
En detalle-top se divide la pantalla en dos columnas:
imagen del perfume
información detallada
Dentro de detalle-img se muestra la imagen del perfume utilizando condicionales de Django.
Si el perfume tiene una imagen registrada, esta se muestra automáticamente. En caso contrario, aparece el mensaje:
Sin imagen
La sección detalle-info muestra información importante del perfume como:
categoría
nombre
marca
país de origen
precio
volumen
género
También se muestra dinámicamente el estado del perfume:
Disponible
Agotado
dependiendo de la información almacenada en la base de datos.
La sección info-grid organiza la información del perfume en cuadros visuales para mejorar la presentación de los datos.
Posteriormente, la sección notas-seccion muestra las notas olfativas del perfume utilizando información obtenida desde el modelo Perfume.
El template utiliza múltiples expresiones de Django como:
{{ perfume.nombre }}
{{ perfume.precio }}
{{ perfume.get_genero_display }}
Estas expresiones permiten mostrar datos dinámicos enviados desde las views.
Además, se utilizan estructuras condicionales de Django mediante:
{% if %}
{% else %}
para controlar cuándo mostrar ciertos elementos en pantalla.
Finalmente, este archivo funciona en conjunto con:
views.py
urls.py
models.py
permitiendo mostrar información detallada de cada perfume de forma dinámica, organizada y visualmente atractiva.

lista.htm
El archivo lista.html es el template principal de la aplicación y se encarga de mostrar todos los perfumes registrados dentro del catálogo virtual.
Este archivo utiliza:
HTML
CSS
templates de Django
para crear una interfaz visual moderna, elegante y dinámica.
Al inicio del documento se configura:
el idioma
la codificación de caracteres
la adaptación para dispositivos móviles
el título principal de la página
También se importan fuentes externas desde Google Fonts para mejorar la apariencia visual del sitio.
Dentro de la etiqueta style se encuentra todo el diseño CSS del proyecto.
Aquí se personalizan elementos como:
colores
tipografías
tamaños
animaciones
efectos visuales
distribución del contenido
diseño responsive
El diseño utiliza tonos oscuros y detalles dorados para representar una perfumería de lujo.
La sección nav corresponde a la barra de navegación superior del sistema.
En esta barra aparecen enlaces hacia:
perfumes de diseñador
perfumes árabes
perfumes de nicho
panel administrador
La sección hero funciona como portada principal del sitio web.
Aquí se muestra:
el nombre de la perfumería
una frase decorativa
un botón para explorar la colección
Posteriormente se crean tres secciones principales del catálogo:
Diseñador
Árabe
Nicho
Cada sección muestra perfumes filtrados según la categoría enviada desde las views.
Dentro de cada categoría se utiliza:
{% for perfume in … %}
para recorrer dinámicamente todos los perfumes registrados en la base de datos.
Cada perfume se muestra mediante una tarjeta visual llamada card.
Dentro de cada tarjeta se presenta:
imagen del perfume
categoría
nombre
marca
mililitros
género
precio
disponibilidad
El template utiliza condicionales de Django para verificar si el perfume tiene imagen registrada.
Si existe una imagen:
se muestra automáticamente
Si no existe:
aparece el texto “Sin imagen”
También se utilizan condicionales para mostrar si un perfume:
está disponible
está agotado
Cada tarjeta funciona como un enlace hacia el detalle individual del perfume utilizando:
{% url ‘detalle_perfume’ perfume.pk %}
Esto permite navegar hacia la vista detallada de cada producto.
Las secciones se encuentran separadas visualmente mediante líneas decorativas y fondos personalizados.
Finalmente, el footer muestra el nombre de la perfumería y el año del proyecto.
Este template trabaja directamente con:
views.py
urls.py
models.py
permitiendo mostrar información dinámica obtenida desde la base de datos en una interfaz visual completamente funcional.
carrito.html
El archivo carrito.html corresponde al template encargado de mostrar el resumen detallado de la colección selecta de productos que un usuario ha añadido a su carrito de compras dentro de la aplicación web.
Este archivo utiliza HTML, CSS y el sistema de templates de Django para crear una interfaz visual elegante, funcional y dinámica.
En la parte inicial del documento se configura la estructura básica de la página, incluyendo:
idioma
codificación de caracteres
adaptación para dispositivos móviles
título personalizado para la sección del carrito
También se importan fuentes externas desde Google Fonts (Playfair Display y Raleway) para mantener la coherencia y mejorar el diseño visual de la página.
Dentro de la etiqueta style se encuentra todo el diseño CSS del template. Aquí se personalizan:
colores
tamaños
tipografías
espacios
diseño responsive para ocultar columnas secundarias en pantallas pequeñas
El diseño utiliza una apariencia moderna y elegante con colores oscuros y detalles dorados para representar la exclusividad y sofisticación de una tienda de perfumes de lujo.
La clase carrito-container organiza todo el contenido principal de la página de manera limpia y simétrica.
La sección volver crea un enlace estilizado que permite al usuario regresar de forma cómoda al catálogo principal de perfumes para continuar explorando.
La sección principal se compone de una tabla estructurada (tabla-carrito) que divide la información de los productos en cuatro columnas esenciales:
Fragancia (Nombre, marca y mililitros)
Precio unitario
Cantidad seleccionada
Subtotal por producto
El template utiliza una estructura condicional de Django mediante:
Django
{% if carrito.items.all %}
{% else %}

Esta lógica controla el flujo visual de la pantalla. Si el carrito contiene elementos, se despliega la tabla con el desglose de los productos y los botones de acción. En caso contrario, la tabla se oculta y aparece dinámicamente el mensaje:
No has añadido ninguna fragancia a tu carrito todavía.
Dentro de la tabla, se utiliza el bucle de Django {% for item in carrito.items.all %} para iterar y renderizar automáticamente cada fila de productos registrados en la base de datos de manera limpia.
Debajo de la tabla, la sección resumen-carrito alinea a la derecha los datos de cierre del pedido, organizando el bloque del total estimado y un botón elegante de confirmación (btn-pedido) con un llamado a la acción exclusivo.
El template utiliza múltiples expresiones de Django y acceso a propiedades de los modelos como:
{{ item.perfume.nombre }}
{{ item.cantidad }}
{{ item.subtotal }}
{{ carrito.total }}
Estas expresiones permiten calcular y mostrar los montos monetarios y las cantidades físicas en tiempo real, datos que son procesados directamente desde el backend.
Finalmente, este archivo funciona en estrecha relación y conjunto con:
views.py (que recupera el carrito del usuario activo)
urls.py (que resuelve la ruta de navegación)
models.py (que calcula los subtotales y el total general mediante propiedades decoradas)
Permitiendo desplegar una experiencia de usuario completamente dinámica, organizada y visualmente atractiva para el cierre de la compra.













EXPLICACIÓN DE MODELS.PY
Carpeta principal (App)
models.py
El archivo models.py es el núcleo de los datos de la aplicación. Define la estructura de la base de datos relacional mediante la programación orientada a objetos de Django (ORM). Cada clase representa una tabla en la base de datos y cada atributo define un campo o columna con restricciones específicas.
Para garantizar un entorno moderno y de alta seguridad, el sistema sustituye los identificadores numéricos tradicionales (AutoIncrement ID) por identificadores únicos globales (UUIDField), haciendo que las URLs de los perfumes y carritos sean indescifrables y más seguras.
Bloques Estructurales del Modelo de Datos
1. Modelo: User (Usuario)
Hereda de AbstractUser, lo que permite a Django mantener todo su sistema nativo de autenticación (contraseñas, sesiones, login) pero añadiendo campos personalizados.
id: Tipo UUID, actúa como llave primaria de forma oculta y automática (editable=False).
is_seller: Un campo booleano (True/False) diseñado para separar la lógica entre los clientes de la tienda y los administradores o vendedores de perfumes.
2. Modelo: Marca
Representa la casa comercial o diseñador de las fragancias (ej. Chanel, Dior, Tom Ford). Es el lado "Uno" en la relación con los perfumes.
nombre y pais_origen: Cadenas de texto estandarizadas (CharField) para clasificar la procedencia de la marca.
3. Modelo: Perfume
Es la entidad central del catálogo de lujo. Almacena las especificaciones técnicas y comerciales de cada fragancia.
GENERO_CHOICES y CATEGORIA_CHOICES: Tuercas de control internas que limitan las opciones en el administrador a catálogos específicos (Hombre, Mujer, Unisex / Diseñador, Árabe, Nicho) usando códigos de un solo carácter para optimizar almacenamiento.
marca: Llave foránea (ForeignKey) que conecta directamente con el modelo Marca. Utiliza on_delete=models.CASCADE para que si una marca es eliminada, sus perfumes asociados se borren automáticamente en cascada. El related_name='perfumes' permite que desde el objeto de una Marca puedas consultar sus productos escribiendo simplemente .perfumes.all().
precio: Un campo decimal controlado (max_digits=8, decimal_places=2) ideal para almacenar valores monetarios exactos sin los errores de redondeo que provocan los números de punto flotante.
imagen e imagen_url: Campos híbridos. Permiten subir un archivo físico al servidor mediante ImageField (guardado en la carpeta perfumes/) o enlazar una imagen externa vía URL de internet.
4. Modelo: Coleccion
Funciona como agrupador temático o estacional de productos (ej. "Tendencias de Verano").
perfumes: Campo de relación Muchos a Muchos (ManyToManyField). Django crea una tabla intermedia transparente para asociar de forma masiva colecciones y fragancias sin exclusividad de ningún lado. Su propiedad blank=True permite crear una colección vacía antes de asignarle artículos.
5. Modelo: Resena
Almacena el feedback de satisfacción, calificaciones y textos descriptivos de la experiencia de los compradores.
perfume: Llave foránea que ata cada comentario a una fragancia específica. El parámetro related_name='resenas' es vital porque es el que limpia las consultas en tu vista de detalle para jalar las opiniones con .resenas.all().
6. Modelo: Carrito
Representa la orden de compra temporal o activa asignada a un cliente.
user: Vinculado al usuario que inició sesión.
Propiedad Dinámica @property def total(self):: Una función decorada que no se guarda estáticamente en la base de datos, sino que calcula el valor monetario acumulado del carrito en tiempo real. Utiliza una expresión generadora (sum(...)) que itera a través de la relación inversa personalizada self.items.all(), sumando los subtotales de cada renglón.
7. Modelo: CarritoItem
Funciona como la tabla intermedia explícita del carrito de compras. Es necesaria para romper la relación de muchos a muchos entre Carrito y Perfume, permitiendo inyectar un dato crucial que no pertenece a ninguno de los dos modelos de forma aislada: la cantidad adquirida.
cantidad: Un entero positivo (PositiveIntegerField) que por defecto inicia en 1.
Meta unique_together: Una regla estricta a nivel de base de datos que impide que un mismo perfume se duplique en renglones diferentes dentro del mismo carrito; en su lugar, obliga al sistema a incrementar únicamente el campo cantidad.
Propiedad Dinámica @property def subtotal(self):: Multiplica el precio actual del perfume por las unidades seleccionadas por el cliente, entregando el costo por renglón de manera inmediata.
Resumen de Conectividad del Backend
Este archivo es la espina dorsal del proyecto. Provee las consultas relacionales y los cálculos automatizados a las funciones de views.py, valida las mutaciones de datos en los formularios del detalle.html y estructura las columnas de despliegue interactivo que se configuran dentro del ecosistema de admin.py.































CONCLUSIONES FINALES
Durante el desarrollo del proyecto PARFUMS se logró comprender de manera práctica cómo funciona una aplicación web creada con Django, aplicando tanto conocimientos de programación como de bases de datos y desarrollo visual. A lo largo del proyecto fue posible observar cómo cada archivo y cada carpeta cumplen una función importante dentro de la estructura general del sistema, permitiendo que todas las partes trabajen de manera organizada y conectada entre sí.
Uno de los aprendizajes más importantes fue entender la arquitectura MTV de Django, ya que gracias a este modelo se pudo separar correctamente la lógica del programa, la base de datos y la interfaz visual. Esto ayudó a mantener el proyecto ordenado y facilitó mucho el proceso de programación. Los modelos permitieron construir toda la estructura de la base de datos, las views se encargaron de procesar la información y los templates hicieron posible mostrar todos los datos de manera dinámica y visualmente atractiva para el usuario.
También fue muy importante aprender a trabajar con modelos y relaciones dentro de Django ORM. En este proyecto se utilizaron relaciones de uno a muchos y muchos a muchos, especialmente entre perfumes, marcas, colecciones, reseñas y carritos de compra. Gracias a esto se pudo entender cómo funcionan las conexiones entre tablas dentro de una base de datos relacional y cómo Django facilita mucho este proceso mediante código Python. El modelo Perfume fue una de las partes más completas del sistema, ya que integró imágenes, categorías, marcas, precios, stock y relaciones con otros modelos.
Otro aspecto importante fue la creación y configuración del entorno de trabajo. Durante el proyecto se aprendió a utilizar entornos virtuales, instalar librerías como Django y Pillow, ejecutar migraciones y trabajar con Git y GitHub para mantener actualizado el proyecto. Todo esto permitió comprender mejor cómo se organiza un proyecto real de desarrollo web y cómo deben administrarse sus dependencias y archivos.
Además, se logró entender la importancia de archivos fundamentales como settings.py, urls.py, views.py y models.py. Por ejemplo, en la imagen mostrada se puede observar el archivo settings.py abierto dentro de Visual Studio Code, el cual contiene gran parte de la configuración principal del proyecto. En este archivo se definieron aspectos esenciales como las aplicaciones instaladas, la configuración de la base de datos SQLite, el manejo de archivos estáticos y multimedia, el modelo de usuario personalizado y diferentes configuraciones internas de Django. Esto permitió comprender que settings.py funciona prácticamente como el centro de control del proyecto, ya que desde ahí se configura gran parte del comportamiento del sistema.
También fue posible observar cómo Visual Studio Code facilita mucho el desarrollo del proyecto, ya que permite visualizar toda la estructura de carpetas y archivos de manera organizada. En la imagen se aprecia la carpeta principal Perfumeria, donde se encuentran archivos importantes como settings.py, urls.py, asgi.py y wsgi.py, además de la aplicación perfumes y la base de datos db.sqlite3. Esto ayudó a identificar cómo se estructura internamente un proyecto Django y cómo cada archivo tiene una función específica dentro del sistema.
El desarrollo de los templates lista.html y detalle.html permitió mejorar habilidades relacionadas con HTML, CSS y templates de Django. Gracias a estos archivos se logró crear una interfaz visual moderna y elegante para la perfumería virtual, utilizando diseños responsivos, tarjetas dinámicas, imágenes y estilos personalizados. Además, se aprendió a utilizar expresiones y estructuras condicionales de Django para mostrar información obtenida directamente desde la base de datos, lo cual hizo que el sitio web funcionara de manera dinámica.
Otro aprendizaje importante fue comprender el funcionamiento de las migraciones en Django. Mediante archivos como 0001_initial.py se pudo observar cómo Django genera automáticamente la estructura de la base de datos a partir de los modelos creados en Python. Esto ayudó a entender cómo se construyen las tablas y relaciones del sistema sin necesidad de escribir manualmente código SQL complejo.
En cuanto al funcionamiento CRUD, el proyecto permitió practicar operaciones fundamentales dentro del desarrollo web, como crear, consultar, modificar y eliminar registros. Estas operaciones son esenciales para prácticamente cualquier sistema moderno y ayudaron a comprender cómo administrar información dentro de una aplicación web real.
Finalmente, este proyecto no solamente ayudó a fortalecer conocimientos técnicos, sino también habilidades relacionadas con organización, lógica de programación y estructura de proyectos. Se logró integrar programación backend, bases de datos, diseño visual y administración del sistema en una sola aplicación funcional. PARFUMS representó una experiencia muy completa para comprender el funcionamiento de Django y el desarrollo web moderno, permitiendo aplicar de forma práctica muchos de los conocimientos vistos durante el curso.

