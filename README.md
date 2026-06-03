<div align="center">

# 🌸 PARFUMS
### Sistema Web de Gestión de Perfumería

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Imágenes-yellow?style=for-the-badge)

---

**Submódulo:** Implementa Base de Datos Relacionales en un Sistema de Información
**Profesor:** José Christian Romero Hernández
**Grupo:** 4 AVPG

---

### 👥 Equipo de Desarrollo

| Alumno |
|--------|
| Camacho Molinares Valentina |
| Flores Bravo Stephanie Naomi |
| Ramos Camargo Kharly Alejandra |
| Rubio Camacho Omar Alejandro |
| Torres Bon Mario Alfredo |
| Velarde Quintero Natalia |

📍 Tijuana, B.C. — 28 de mayo de 2026

</div>

---

## 📋 Índice

1. [Introducción](#-introducción)
2. [Objetivo del Proyecto](#-objetivo-del-proyecto)
3. [Instalación del Proyecto](#-instalación-del-proyecto)
4. [Estructura del Proyecto](#-estructura-del-proyecto)
   - [Carpeta perfumeria](#carpeta-perfumeria)
   - [Carpeta perfumes](#carpeta-perfumes)
   - [Carpeta migrations](#carpeta-migrations)
   - [Carpeta templates](#carpeta-templates)
5. [Explicación de models.py](#-explicación-de-modelspy)
6. [Relaciones de Base de Datos](#-relaciones-de-base-de-datos)
7. [Explicación de admin.py](#-explicación-de-adminpy)
8. [Explicación de views.py](#-explicación-de-viewspy)
9. [Explicación de urls.py](#-explicación-de-urlspy)
10. [Funcionamiento CRUD](#-funcionamiento-crud)
11. [Diseño de la Base de Datos](#-diseño-de-la-base-de-datos)
12. [Conclusiones](#-conclusiones)

---

## 📖 Introducción

El presente proyecto consiste en el desarrollo de un sistema web para la gestión y visualización de una perfumería en línea, denominada **Perfumería Élite**, construido utilizando el framework Django de Python como tecnología principal. El sistema permite administrar un catálogo completo de fragancias organizadas en tres categorías principales: perfumes de diseñador, perfumes árabes y perfumes de nicho, abarcando las marcas más reconocidas a nivel mundial como Chanel, Dior, Tom Ford, Amouage, Creed y Maison Francis Kurkdjian, entre muchas otras.

El sistema fue desarrollado con el objetivo de aplicar los conocimientos adquiridos en el curso sobre bases de datos relacionales y desarrollo web, implementando los conceptos fundamentales de modelado de datos mediante el uso del ORM de Django. La base de datos del proyecto contempla relaciones de **uno a muchos**, como la existente entre una marca y sus perfumes, así como relaciones de **muchos a muchos**, como la que existe entre los perfumes y las colecciones temáticas, y la que se establece entre los usuarios y los perfumes a través del carrito de compras.

La estructura del proyecto comprende seis modelos principales: `Marca`, `Perfume`, `Colección`, `Reseña`, `Carrito` y `CarritoItem`, cada uno diseñado para cubrir una necesidad específica dentro del sistema. El modelo de Perfume concentra la información central del catálogo, incluyendo nombre, precio, volumen en mililitros, género, categoría, notas olfativas, stock disponible e imagen de referencia. Las colecciones permiten agrupar perfumes bajo temáticas especiales como colecciones de temporada o selecciones por género, mientras que las reseñas permiten registrar la opinión y calificación de los clientes sobre cada fragancia.

La interfaz del sistema cuenta con un panel de administración robusto, desarrollado sobre el administrador nativo de Django, en el cual es posible realizar operaciones completas de alta, consulta, modificación y baja de registros para cada uno de los modelos. Adicionalmente, el sistema cuenta con una interfaz pública de visualización del catálogo, diseñada con un estilo elegante y oscuro acorde a la identidad visual de una perfumería de lujo, donde los usuarios pueden explorar el catálogo completo, consultar el detalle de cada fragancia y visualizar las reseñas de otros clientes.

El proyecto fue desarrollado en su totalidad utilizando **Python 3.13**, **Django 5.2**, **SQLite** como motor de base de datos y **Visual Studio Code** como entorno de desarrollo, siguiendo buenas prácticas de organización de código y estructura de proyectos web.

---

## 🎯 Objetivo del Proyecto

El objetivo principal del proyecto PARFUMS es desarrollar una aplicación web funcional utilizando el lenguaje de programación Python y el framework Django, aplicando los conocimientos de programación, desarrollo web y bases de datos relacionales aprendidos durante el curso.

El sistema fue diseñado para administrar una tienda de perfumes mediante una plataforma que permita registrar, visualizar, modificar y eliminar información relacionada con perfumes, marcas, colecciones, reseñas y carritos de compra.

### 🏗️ Arquitectura MTV

A nivel de programación, el proyecto tiene como finalidad implementar correctamente la arquitectura **MTV (Model - Template - View)** de Django, permitiendo la interacción entre:

- 📦 Los modelos de base de datos
- 👁️ Las vistas del sistema
- 🔗 Las URLs
- 🎨 Las interfaces visuales creadas con templates HTML

### 🔗 Relaciones Implementadas

| Tipo de Relación | Ejemplo en el Proyecto |
|-----------------|----------------------|
| 🔷 Uno a Muchos | Una Marca → Muchos Perfumes |
| 🔶 Muchos a Muchos | Perfumes ↔ Colecciones |
| 🔶 Muchos a Muchos | Usuarios ↔ Perfumes (via CarritoItem) |

### ⚙️ Operaciones CRUD

Se implementaron operaciones **CRUD** completas desde el panel administrativo de Django:

| Operación | Descripción |
|-----------|-------------|
| ✅ **Crear** | Registrar nuevos perfumes, marcas, colecciones y reseñas |
| 👁️ **Leer** | Visualizar todo el catálogo con filtros y búsqueda |
| ✏️ **Actualizar** | Modificar información existente |
| 🗑️ **Eliminar** | Borrar registros del sistema |

### 💪 Habilidades Fortalecidas

- Organización de código y estructura de proyectos
- Manejo de rutas y URLs
- Uso de clases y modelos con Django ORM
- Manipulación de datos relacionales
- Manejo de imágenes con **Pillow**
- Control de versiones mediante **Git y GitHub**

---

## 🚀 Instalación del Proyecto

Para ejecutar correctamente el proyecto PARFUMS fue necesario instalar y configurar diferentes herramientas y dependencias de programación.

Primero se creó un entorno virtual utilizando Python para mantener organizadas las librerías del proyecto y evitar conflictos con otros programas instalados en la computadora.

**1. Crear entorno virtual**
```bash
python -m venv venv
```

Después se activó el entorno virtual para comenzar a trabajar dentro del proyecto.

**2. Activar entorno virtual**
```bash
venv\Scripts\activate
```

Luego se instaló Django versión 5.2, el framework principal utilizado para desarrollar toda la aplicación web.

**3. Instalar Django**
```bash
pip install django==5.2
```

También se instaló la librería Pillow, utilizada para el manejo y almacenamiento de imágenes dentro del sistema, especialmente para las imágenes de perfumes.

**4. Instalar Pillow**
```bash
pip install pillow
```

Posteriormente se clonó el repositorio del proyecto desde GitHub utilizando Git.

**5. Clonar el repositorio**
```bash
git clone https://github.com/Alxjandrz/PARFUMS.git
```

**6. Ingresar a la carpeta del proyecto**
```bash
cd PARFUMS
```

Para mantener el proyecto actualizado se utilizaron los comandos:

**7. Mantener el proyecto actualizado**
```bash
git fetch
git pull
```

Finalmente se abrió el proyecto en Visual Studio Code para continuar con el desarrollo y programación del sistema.

**8. Abrir en Visual Studio Code**
```bash
code .
```

Una vez configurado todo el entorno, se ejecutaron las migraciones de la base de datos y se inició el servidor de Django.

**9. Ejecutar migraciones e iniciar servidor**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

> 🌐 El sistema estará disponible en `http://127.0.0.1:8000`

---

## 📁 Estructura del Proyecto

<img width="1024" height="1536" alt="Copilot_20260601_170431" src="https://github.com/user-attachments/assets/9838f032-0d3d-48fe-b2e2-06d974b2a2e4" />


### Carpeta perfumeria

#### 📄 `asgi.py`

El archivo `asgi.py` forma parte de la configuración principal del proyecto Django y permite que la aplicación pueda comunicarse correctamente con el servidor web.

Su función principal es preparar y ejecutar el proyecto utilizando ASGI, una tecnología que permite manejar múltiples conexiones y procesos de manera más eficiente.

En este archivo también se indica cuál es la configuración principal del proyecto, utilizando el archivo `settings.py` de la carpeta Perfumeria. Finalmente, se crea la aplicación principal de Django para que el servidor pueda ejecutar correctamente el sistema web.

```python
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Perfumeria.settings')
application = get_asgi_application()
```

---

#### 📄 `settings.py`

El archivo `settings.py` es uno de los archivos más importantes del proyecto, ya que contiene toda la configuración principal de Django y controla el funcionamiento general de la aplicación.

| Configuración | Descripción |
|--------------|-------------|
| `BASE_DIR` | Define la ruta principal del proyecto para ubicar carpetas y archivos |
| `SECRET_KEY` | Clave secreta para proporcionar seguridad interna |
| `DEBUG = True` | Permite visualizar errores durante el desarrollo |
| `INSTALLED_APPS` | Registra todas las aplicaciones incluyendo `perfumes` |
| `MIDDLEWARE` | Herramientas para seguridad, sesiones, autenticación y mensajes |
| `ROOT_URLCONF` | Archivo principal encargado de manejar las URLs |
| `TEMPLATES` | Permite utilizar archivos HTML para la interfaz visual |
| `DATABASES` | Configura SQLite almacenada en `db.sqlite3` |
| `AUTH_PASSWORD_VALIDATORS` | Validaciones de seguridad para contraseñas |
| `STATIC_URL` | Manejo de archivos estáticos (CSS, JS, imágenes) |
| `AUTH_USER_MODEL` | Modelo de usuario personalizado `perfumes.User` |
| `MEDIA_URL / MEDIA_ROOT` | Configuración para almacenar y mostrar imágenes de perfumes |

---

#### 📄 `urls.py`

El archivo `urls.py` se encarga de manejar las rutas principales del proyecto Django y conectar las diferentes partes de la aplicación.

```python
urlpatterns = [
    path('admin/',    admin.site.urls),
    path('perfumes/', include('perfumes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- `admin/` — Acceso al panel administrativo de Django
- `perfumes/` — Conecta todas las URLs de la aplicación perfumes usando `include()`
- `static()` — Permite mostrar correctamente las imágenes almacenadas en la carpeta `media`

Gracias a este archivo, el sistema puede conectar las URLs, las vistas, los modelos y las interfaces HTML, permitiendo el correcto funcionamiento de toda la aplicación web.

---

#### 📄 `wsgi.py`

El archivo `wsgi.py` forma parte de la configuración principal del proyecto Django y se encarga de permitir la comunicación entre el servidor web y la aplicación.

Su función principal es preparar el proyecto para que pueda ejecutarse correctamente en servidores web compatibles con WSGI. En este archivo se importa la configuración principal del proyecto utilizando `settings.py` y se crea la aplicación principal de Django, la cual será utilizada por el servidor para ejecutar el sistema web. Este archivo es importante porque permite que la aplicación pueda funcionar correctamente cuando se despliega en un entorno de producción.

```python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Perfumeria.settings')
application = get_wsgi_application()
```

---

### Carpeta perfumes

#### 📄 `admin.py`

El archivo `admin.py` configura el panel administrativo con funcionalidades avanzadas para gestionar todos los modelos del sistema.

**Panel de Perfumes:**
- `list_display` — Muestra nombre, marca, precio, ml, género, categoría, stock y vista previa de imagen en miniatura
- `list_filter` — Filtros laterales por categoría, género, disponibilidad y marca
- `search_fields` — Búsqueda por nombre de perfume y nombre de marca
- `fieldsets` — Organiza campos en secciones: Información general, Precio y stock, Descripción, Imagen y Fecha de registro
- `ver_imagen` — Muestra miniatura de imagen directamente en el listado del panel
- `ver_imagen_detalle` — Vista previa grande dentro del formulario de edición

**Panel de Colecciones:**
- `filter_horizontal` — Selector visual doble para asignar perfumes a colecciones de forma cómoda
- `total_perfumes` — Columna dinámica que muestra el conteo de perfumes por colección

**Panel de Reseñas:**
- `list_filter` — Filtros por calificación y perfume
- `ordering` — Ordenado por fecha descendente (más recientes primero)

**Panel de Carritos:**
- `CarritoItemInline` — Muestra los productos del carrito directamente dentro del formulario de cada carrito usando `TabularInline`
- `total_items` — Contador dinámico de productos en el carrito
- `total_carrito` — Calcula y muestra el total monetario en tiempo real

**Panel de CarritoItems:**
- `get_usuario` — Muestra el nombre de usuario del dueño del carrito
- `get_fecha` — Muestra la fecha en que se realizó el pedido

---

#### 📄 `apps.py`

El archivo `apps.py` se encarga de configurar la aplicación `perfumes` dentro del proyecto Django mediante la clase `PerfumesConfig`.

- `default_auto_field` — Configura el tipo de identificador automático de los modelos
- `name = 'perfumes'` — Indica el nombre oficial de la aplicación registrada dentro del proyecto Django

Este archivo ayuda a que Django reconozca correctamente la aplicación `perfumes` y pueda integrarla con el resto del sistema.

```python
from django.apps import AppConfig

class PerfumesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfumes'
```

---

#### 📄 `models.py`

El archivo `models.py` es uno de los más importantes del proyecto, ya que contiene todos los modelos de la base de datos. Cada modelo representa una tabla distinta dentro del sistema y permite almacenar información relacionada con la perfumería.

Primero se importan las herramientas necesarias de Django y la librería `uuid`, utilizada para generar identificadores únicos para cada registro.

El modelo **User** representa a los usuarios del sistema. Este modelo hereda de `AbstractUser`, lo que permite utilizar el sistema de autenticación de Django y agregar nuevas características personalizadas. En este caso, se añadió el campo `is_seller` para identificar si el usuario es vendedor. Además, se utiliza UUID como identificador principal para mejorar la seguridad del sistema.

El modelo **Marca** representa las marcas de perfumes. Cada marca almacena nombre y país de origen. Este modelo tiene una relación de Uno a Muchos con el modelo Perfume, lo que significa que una marca puede tener muchos perfumes registrados.

El modelo **Perfume** representa los productos principales del sistema. Aquí se almacena información como nombre, marca, precio, stock, mililitros, género, categoría, notas olfativas e imágenes. También se agregaron opciones de selección para género y categoría, facilitando el ingreso de datos desde el panel administrativo. Este modelo tiene varias relaciones importantes: pertenece a una marca, puede tener muchas reseñas, puede estar en muchas colecciones y puede agregarse a muchos carritos. Además, se implementó `ImageField` para permitir subir imágenes de perfumes al sistema.

El modelo **Coleccion** sirve para agrupar perfumes dentro de diferentes categorías o temporadas. Este modelo utiliza una relación de Muchos a Muchos con Perfume, lo que significa que una colección puede contener muchos perfumes y un perfume puede pertenecer a muchas colecciones. Esta es una de las relaciones más importantes del proyecto porque demuestra el uso de relaciones complejas dentro de bases de datos relacionales.

El modelo **Resena** permite almacenar opiniones y calificaciones de clientes sobre perfumes. Cada reseña contiene nombre del cliente, calificación, comentario y fecha. Este modelo tiene una relación de Uno a Muchos con Perfume, ya que un perfume puede tener muchas reseñas.

El modelo **Carrito** representa el carrito de compras de cada usuario. Cada carrito pertenece a un usuario específico y almacena la fecha de creación. También se implementó una propiedad llamada `total`, la cual calcula automáticamente el precio total de todos los productos agregados al carrito.

El modelo **CarritoItem** funciona como una tabla intermedia entre Carrito y Perfume. Este modelo permite almacenar el perfume agregado, la cantidad seleccionada y el subtotal de la compra. Además, se implementó una restricción para evitar que un mismo perfume se repita varias veces dentro del mismo carrito.

En general, este archivo es el encargado de estructurar toda la base de datos del proyecto y definir las relaciones entre los diferentes modelos del sistema.

```python
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_seller = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Perfume(models.Model):
    GENERO_CHOICES = [('H','Hombre'),('M','Mujer'),('U','Unisex')]
    CATEGORIA_CHOICES = [('D','Disenador'),('A','Arabe'),('N','Nicho')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='perfumes')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    ml = models.IntegerField(help_text="Mililitros")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, default='D')
    notas_olfativas = models.TextField(blank=True)
    en_stock = models.BooleanField(default=True)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    imagen = models.ImageField(upload_to='perfumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre} - {self.marca.nombre}"

class Coleccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    perfumes = models.ManyToManyField(Perfume, related_name='colecciones', blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre

class Resena(models.Model):
    CALIFICACION_CHOICES = [(1,'1 - Malo'),(2,'2 - Regular'),(3,'3 - Bueno'),(4,'4 - Muy bueno'),(5,'5 - Excelente')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE, related_name='resenas')
    nombre_cliente = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=CALIFICACION_CHOICES)
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre_cliente} - {self.perfume.nombre} ({self.calificacion})"

class Carrito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carritos')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Carrito de {self.user.username}"
    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())

class CarritoItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE, related_name='carrito_items')
    cantidad = models.PositiveIntegerField(default=1)
    class Meta:
        unique_together = ('carrito', 'perfume')
    @property
    def subtotal(self):
        return self.perfume.precio * self.cantidad
    def __str__(self):
        return f"{self.perfume.nombre} x {self.cantidad} — {self.carrito.user.username}"
```

---

#### 📄 `tests.py`

El archivo `tests.py` se utiliza para realizar pruebas dentro del proyecto Django. Su función principal es verificar que las diferentes partes del sistema funcionen correctamente, evitando errores durante el desarrollo de la aplicación.

En este caso, el archivo únicamente importa `TestCase` desde Django, una herramienta utilizada para crear pruebas automáticas. Actualmente el archivo no contiene pruebas programadas, lo que indica que está preparado para agregar pruebas en el futuro, como:

- Pruebas de modelos
- Pruebas de vistas
- Validaciones de formularios
- Funcionamiento de URLs

Aunque en este proyecto no se implementaron pruebas automáticas, el archivo forma parte de la estructura estándar de Django y permite expandir el sistema posteriormente.

```python
from django.test import TestCase

# Create your tests here.
```

---

#### 📄 `urls.py` *(de la app perfumes)*

El archivo `urls.py` de la aplicación perfumes se encarga de definir las rutas internas del sistema y conectar las URLs con las views correspondientes.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.lista_perfumes,     name='lista_perfumes'),
    path('<uuid:pk>/',              views.detalle_perfume,    name='detalle_perfume'),
    path('<uuid:pk>/agregar/',      views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/',                views.ver_carrito,        name='ver_carrito'),
    path('<uuid:pk>/resena/',       views.agregar_resena,     name='agregar_resena'),
]
```

| Ruta | Vista | Descripción |
|------|-------|-------------|
| `''` | `lista_perfumes` | Página principal del catálogo |
| `<uuid:pk>/` | `detalle_perfume` | Detalle individual de cada perfume |
| `<uuid:pk>/agregar/` | `agregar_al_carrito` | Agrega un perfume al carrito del usuario |
| `carrito/` | `ver_carrito` | Muestra el carrito del usuario activo |
| `<uuid:pk>/resena/` | `agregar_resena` | Publica una nueva reseña de un perfume |

El parámetro `pk` representa la clave primaria del perfume y permite identificar qué registro debe mostrarse. Gracias a este archivo, las URLs pueden comunicarse correctamente con las views para mostrar información dinámica dentro de la aplicación web.

---

#### 📄 `views.py`

El archivo `views.py` contiene la lógica principal de la aplicación y se encarga de conectar los modelos con los templates para mostrar información al usuario.

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfume, Coleccion, Resena, Carrito, CarritoItem

def lista_perfumes(request):
    disenador = Perfume.objects.filter(categoria='D')
    arabes    = Perfume.objects.filter(categoria='A')
    nicho     = Perfume.objects.filter(categoria='N')
    return render(request, 'perfumes/lista.html', {
        'disenador': disenador,
        'arabes':    arabes,
        'nicho':     nicho,
    })

def detalle_perfume(request, pk):
    perfume     = get_object_or_404(Perfume, pk=pk)
    resenas     = perfume.resenas.all().order_by('-fecha')
    colecciones = perfume.colecciones.all()
    carrito     = None
    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(user=request.user)
    return render(request, 'perfumes/detalle.html', {
        'perfume':     perfume,
        'resenas':     resenas,
        'colecciones': colecciones,
        'carrito':     carrito,
    })

@login_required
def agregar_al_carrito(request, pk):
    if request.method == 'POST':
        perfume  = get_object_or_404(Perfume, pk=pk)
        cantidad = int(request.POST.get('cantidad', 1))
        carrito, _ = Carrito.objects.get_or_create(user=request.user)
        item, item_created = CarritoItem.objects.get_or_create(carrito=carrito, perfume=perfume)
        if not item_created:
            item.cantidad += cantidad
        else:
            item.cantidad = cantidad
        item.save()
        return redirect('ver_carrito')
    return redirect('detalle_perfume', pk=pk)

@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(user=request.user)
    return render(request, 'perfumes/carrito.html', {'carrito': carrito})

def agregar_resena(request, pk):
    if request.method == 'POST':
        perfume        = get_object_or_404(Perfume, pk=pk)
        nombre_cliente = request.POST.get('nombre_cliente', '').strip()
        calificacion   = request.POST.get('calificacion')
        comentario     = request.POST.get('comentario', '').strip()
        if nombre_cliente and calificacion and comentario:
            Resena.objects.create(
                perfume=perfume,
                nombre_cliente=nombre_cliente,
                calificacion=int(calificacion),
                comentario=comentario
            )
    return redirect('detalle_perfume', pk=pk)
```

La función `lista_perfumes` se encarga de mostrar todos los perfumes organizados por categorías, realizando consultas con `Perfume.objects.filter()` para separar los perfumes en diseñador, árabes y nicho, enviando toda la información al template `lista.html`.

La función `detalle_perfume` se encarga de mostrar la información específica de un perfume seleccionado. Utiliza `get_object_or_404` para buscar el perfume mediante su identificador — si no existe, Django mostrará automáticamente un error 404. Luego obtiene las reseñas ordenadas por fecha y las colecciones relacionadas, enviando todo al template `detalle.html`.

Gracias a este archivo, las views pueden comunicarse con los modelos, las URLs y los templates, permitiendo que la aplicación funcione dinámicamente y muestre información actualizada al usuario.

La función `agregar_al_carrito` está protegida con `@login_required` y solo acepta peticiones `POST`. Obtiene o crea un carrito para el usuario activo, luego obtiene o crea el `CarritoItem` correspondiente. Si el producto ya existía en el carrito, incrementa la cantidad; de lo contrario, la establece con el valor del formulario.

La función `ver_carrito` también requiere login y obtiene o crea el carrito del usuario activo, enviándolo al template `carrito.html` para su visualización.

La función `agregar_resena` no requiere login y procesa el formulario de reseña del template `detalle.html`. Valida que los tres campos requeridos (nombre, calificación y comentario) no estén vacíos antes de crear el registro en la base de datos.

---

### Carpeta migrations

#### 📄 `0001_initial.py`

El archivo `0001_initial.py` corresponde a la primera migración creada por Django para el proyecto. Las migraciones son archivos que permiten crear y modificar automáticamente la estructura de la base de datos a partir de los modelos definidos en `models.py`.

Este archivo contiene todas las instrucciones necesarias para construir las tablas principales del sistema dentro de la base de datos. La clase `Migration` representa la migración principal del proyecto y contiene todas las operaciones que Django ejecutará en la base de datos.

| Modelo creado | Tabla generada | Descripción |
|--------------|---------------|-------------|
| `Marca` | `perfumes_marca` | Nombre y país de origen de marcas |
| `User` | `perfumes_user` | Usuarios personalizados del sistema |
| `Carrito` | `perfumes_carrito` | Carritos de compra por usuario |
| `Perfume` | `perfumes_perfume` | Tabla principal de fragancias |
| `Coleccion` | `perfumes_coleccion` | Agrupaciones temáticas |
| `CarritoItem` | `perfumes_carritoitem` | Tabla intermedia carrito-perfume |
| `Resena` | `perfumes_resena` | Opiniones y calificaciones |

Dentro de `dependencies` se establece la dependencia con el sistema de autenticación de Django, permitiendo utilizar usuarios personalizados. En general, este archivo es el encargado de construir toda la estructura inicial de la base de datos del proyecto y establecer las relaciones entre los diferentes modelos del sistema.

---

### Carpeta templates

#### 📄 `detalle.html`

El archivo `detalle.html` corresponde al template encargado de mostrar la información detallada de cada perfume dentro de la aplicación web. Este archivo utiliza HTML, CSS y el sistema de templates de Django para crear una interfaz visual elegante y dinámica.

Al inicio del documento se configura la estructura básica de la página incluyendo idioma, codificación, adaptación para dispositivos móviles y título dinámico con el nombre del perfume. También se importan fuentes externas desde Google Fonts para mejorar el diseño visual.

El diseño utiliza una apariencia moderna y elegante con **colores oscuros y detalles dorados** para representar una tienda de perfumes de lujo.

La sección `detalle-top` divide la pantalla en dos columnas: imagen del perfume e información detallada. Dentro de `detalle-img` se muestra la imagen del perfume utilizando condicionales de Django: si el perfume tiene una imagen registrada, esta se muestra automáticamente. Si tiene URL de imagen externa, se muestra esa. En caso contrario, aparece el mensaje "Sin imagen".

La sección `detalle-info` muestra información importante:
- Categoría, nombre, marca y país de origen
- Precio en MXN con formato elegante
- Grid informativo con volumen, género y stock disponible
- Estado de disponibilidad (Disponible / Agotado)
- Notas olfativas con borde decorativo dorado

El template utiliza expresiones de Django como `{{ perfume.nombre }}`, `{{ perfume.precio }}` y `{{ perfume.get_genero_display }}` para mostrar datos dinámicos. También muestra las **colecciones** a las que pertenece el perfume como badges dorados y las **reseñas** de clientes con calificación en estrellas generada dinámicamente mediante un bucle `{% for i in "12345" %}`.

---

#### 📄 `lista.html`

El archivo `lista.html` es el template principal de la aplicación y se encarga de mostrar todos los perfumes registrados dentro del catálogo virtual, utilizando HTML, CSS y templates de Django para crear una interfaz visual moderna, elegante y dinámica.

La sección `nav` corresponde a la barra de navegación superior fija del sistema con enlaces hacia perfumes de diseñador, árabes, de nicho y el panel administrador.

La sección `hero` funciona como portada principal del sitio web mostrando el nombre de la perfumería, una frase decorativa y un botón para explorar la colección.

Posteriormente se crean **tres secciones principales** del catálogo:

| Sección | Categoría | Fondo |
|---------|-----------|-------|
| Diseñador | `categoria='D'` | Oscuro estándar |
| Árabe | `categoria='A'` | Degradado dorado oscuro |
| Nicho | `categoria='N'` | Degradado púrpura oscuro |

Dentro de cada categoría se utiliza `{% for perfume in ... %}` para recorrer dinámicamente todos los perfumes. Cada perfume se muestra mediante una **tarjeta visual** (`card`) que presenta:
- Imagen del perfume (subida o por URL, con fallback "Sin imagen")
- Categoría, nombre y marca
- Badges de mililitros y género
- Precio en MXN
- Indicador de disponibilidad

Cada tarjeta funciona como enlace hacia el detalle individual del perfume utilizando `{% url 'detalle_perfume' perfume.pk %}`. El footer muestra el nombre de la perfumería y el año del proyecto.

---

#### 📄 `carrito.html`

El archivo `carrito.html` corresponde al template encargado de mostrar el resumen detallado de la colección selecta de productos que un usuario ha añadido a su carrito de compras dentro de la aplicación web. Este archivo utiliza HTML, CSS y el sistema de templates de Django para crear una interfaz visual elegante, funcional y dinámica.

También se importan fuentes externas desde Google Fonts (Playfair Display y Raleway) para mantener la coherencia visual de todo el sistema.

La sección principal se compone de una tabla estructurada (`tabla-carrito`) que divide la información de los productos en cuatro columnas esenciales:

| Columna | Descripción |
|---------|-------------|
| Fragancia | Nombre, marca y mililitros del producto |
| Precio unitario | Precio individual del perfume |
| Cantidad | Unidades seleccionadas |
| Subtotal | Precio × Cantidad por producto |

El template utiliza una estructura condicional de Django:

```django
{% if carrito.items.all %}
    {# Muestra la tabla con productos #}
{% else %}
    No has añadido ninguna fragancia a tu carrito todavía.
{% endif %}
```

Dentro de la tabla, se utiliza el bucle `{% for item in carrito.items.all %}` para iterar y renderizar automáticamente cada fila de productos registrados en la base de datos.

Debajo de la tabla, la sección `resumen-carrito` alinea a la derecha los datos de cierre del pedido, organizando el bloque del total estimado y un botón elegante de confirmación.

El template utiliza expresiones de Django y acceso a propiedades de los modelos como:
- `{{ item.perfume.nombre }}` — nombre del producto
- `{{ item.cantidad }}` — unidades seleccionadas
- `{{ item.subtotal }}` — costo por renglón calculado en tiempo real
- `{{ carrito.total }}` — total general del carrito

Finalmente, este archivo funciona en estrecha relación con `views.py` (que recupera el carrito del usuario activo), `urls.py` (que resuelve la ruta de navegación) y `models.py` (que calcula los subtotales y el total general mediante propiedades decoradas).

---

## 🗄️ Explicación de models.py

El archivo `models.py` es el núcleo de los datos de la aplicación. Define la estructura de la base de datos relacional mediante la programación orientada a objetos de Django (ORM). Cada clase representa una tabla en la base de datos y cada atributo define un campo o columna con restricciones específicas.

> 💡 Para garantizar un entorno moderno y de alta seguridad, el sistema sustituye los identificadores numéricos tradicionales (AutoIncrement ID) por **identificadores únicos globales (UUIDField)**, haciendo que las URLs de los perfumes y carritos sean indescifrables y más seguras.

### 👤 Bloque 1: Modelo User

Hereda de `AbstractUser`, lo que permite a Django mantener todo su sistema nativo de autenticación (contraseñas, sesiones, login) pero añadiendo campos personalizados.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | UUIDField | Llave primaria única, oculta y automática (`editable=False`) |
| `is_seller` | BooleanField | Separa la lógica entre clientes y administradores o vendedores |

### 🏷️ Bloque 2: Modelo Marca

Representa la casa comercial o diseñador de las fragancias (ej. Chanel, Dior, Tom Ford). Es el lado "Uno" en la relación con los perfumes.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | UUIDField | Llave primaria |
| `nombre` | CharField | Nombre de la marca |
| `pais_origen` | CharField | País de procedencia |

### 🌸 Bloque 3: Modelo Perfume

Es la entidad central del catálogo de lujo. Almacena las especificaciones técnicas y comerciales de cada fragancia.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | UUIDField | Llave primaria |
| `nombre` | CharField | Nombre del perfume |
| `marca` | ForeignKey | Llave foránea → Marca (on_delete=CASCADE) |
| `precio` | DecimalField | Valor monetario exacto (max_digits=8, decimal_places=2) |
| `stock` | PositiveIntegerField | Unidades disponibles |
| `ml` | IntegerField | Volumen en mililitros |
| `genero` | CharField | H / M / U con GENERO_CHOICES |
| `categoria` | CharField | D / A / N con CATEGORIA_CHOICES |
| `notas_olfativas` | TextField | Descripción de la fragancia |
| `en_stock` | BooleanField | Disponibilidad del producto |
| `imagen` | ImageField | Imagen subida al servidor (carpeta `perfumes/`) |
| `imagen_url` | URLField | Enlace externo de imagen |
| `created_at` | DateTimeField | Fecha de registro automática |

> 🔑 `marca` utiliza `on_delete=models.CASCADE` para que si una marca es eliminada, sus perfumes asociados se borren automáticamente. El `related_name='perfumes'` permite consultar los productos de una marca escribiendo simplemente `.perfumes.all()`.

> 💰 `precio` utiliza `DecimalField` en lugar de `FloatField` para evitar errores de redondeo en valores monetarios exactos.

### 🗂️ Bloque 4: Modelo Coleccion

Funciona como agrupador temático o estacional de productos (ej. "Tendencias de Verano").

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | UUIDField | Llave primaria |
| `nombre` | CharField | Nombre de la colección |
| `descripcion` | TextField | Descripción temática |
| `perfumes` | ManyToManyField | Relación N:M con Perfume |
| `fecha_inicio` | DateField | Inicio de la colección |
| `fecha_fin` | DateField | Fin de la colección |

> Django crea una tabla intermedia transparente para la relación N:M. La propiedad `blank=True` permite crear una colección vacía antes de asignarle artículos.

### ⭐ Bloque 5: Modelo Resena

Almacena el feedback de satisfacción, calificaciones y textos descriptivos de la experiencia de los compradores.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | UUIDField | Llave primaria |
| `perfume` | ForeignKey | Llave foránea → Perfume |
| `nombre_cliente` | CharField | Nombre del cliente |
| `calificacion` | IntegerField | Del 1 al 5 con CALIFICACION_CHOICES |
| `comentario` | TextField | Opinión detallada |
| `fecha` | DateField | Fecha automática |

> El parámetro `related_name='resenas'` permite consultar todas las reseñas de un perfume con `.resenas.all()` directamente desde las vistas.

### 🛒 Bloque 6: Modelo Carrito

Representa la orden de compra temporal o activa asignada a un cliente.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | UUIDField | Llave primaria |
| `user` | ForeignKey | Vinculado al usuario activo |
| `created_at` | DateTimeField | Fecha de creación |
| `total` | @property | Calcula el valor monetario acumulado en tiempo real |

> La propiedad dinámica `@property def total(self)` no se guarda en la base de datos, sino que calcula el valor acumulado del carrito en tiempo real utilizando una expresión generadora `sum(...)` que itera a través de `self.items.all()`.

### 🧾 Bloque 7: Modelo CarritoItem

Funciona como la tabla intermedia explícita del carrito de compras. Es necesaria para romper la relación de muchos a muchos entre Carrito y Perfume, permitiendo inyectar un dato crucial que no pertenece a ninguno de los dos modelos de forma aislada: **la cantidad adquirida**.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | UUIDField | Llave primaria |
| `carrito` | ForeignKey | Relación con Carrito |
| `perfume` | ForeignKey | Relación con Perfume |
| `cantidad` | PositiveIntegerField | Unidades (default=1) |
| `subtotal` | @property | Precio × Cantidad en tiempo real |

> 🔒 `unique_together = ('carrito', 'perfume')` — Regla estricta a nivel de base de datos que impide que un mismo perfume se duplique en renglones diferentes dentro del mismo carrito; en su lugar, obliga al sistema a incrementar únicamente el campo `cantidad`.

> La propiedad `@property def subtotal(self)` multiplica el precio actual del perfume por las unidades seleccionadas, entregando el costo por renglón de manera inmediata.

---

## 🔗 Relaciones de Base de Datos

```
                    ┌──────────┐
                    │  Marca   │
                    └────┬─────┘
                         │ 1
                         │ Uno a Muchos
                         │ N
                    ┌────▼─────┐       ┌────────────┐
                    │ Perfume  ├───────┤  Coleccion │
                    └────┬─────┘  N:M  └────────────┘
                         │
              ┌──────────┼──────────┐
              │ N        │ N        │ N
        ┌─────▼──┐  ┌────▼──────┐  └──────────────┐
        │ Resena │  │CarritoItem│              (más)
        └────────┘  └────┬──────┘
                         │
                    ┌────▼──────┐       ┌──────┐
                    │  Carrito  ├───────┤ User │
                    └───────────┘  N:1  └──────┘
```

| Relación | Tipo | Descripción |
|----------|------|-------------|
| Marca → Perfume | 🔷 Uno a Muchos | Una marca puede tener muchos perfumes |
| Perfume → Resena | 🔷 Uno a Muchos | Un perfume puede tener muchas reseñas |
| User → Carrito | 🔷 Uno a Muchos | Un usuario puede tener muchos carritos |
| Perfume ↔ Coleccion | 🔶 Muchos a Muchos | Un perfume puede estar en muchas colecciones y viceversa |
| Carrito ↔ Perfume | 🔶 Muchos a Muchos | Via CarritoItem con campo de cantidad extra |

---

## 📝 Conclusiones

Durante el desarrollo del proyecto PARFUMS se logró comprender de manera práctica cómo funciona una aplicación web creada con Django, aplicando tanto conocimientos de programación como de bases de datos y desarrollo visual. A lo largo del proyecto fue posible observar cómo cada archivo y cada carpeta cumplen una función importante dentro de la estructura general del sistema, permitiendo que todas las partes trabajen de manera organizada y conectada entre sí.

Uno de los aprendizajes más importantes fue entender la **arquitectura MTV de Django**, ya que gracias a este modelo se pudo separar correctamente la lógica del programa, la base de datos y la interfaz visual. Esto ayudó a mantener el proyecto ordenado y facilitó mucho el proceso de programación. Los modelos permitieron construir toda la estructura de la base de datos, las views se encargaron de procesar la información y los templates hicieron posible mostrar todos los datos de manera dinámica y visualmente atractiva para el usuario.

También fue muy importante aprender a trabajar con **modelos y relaciones dentro de Django ORM**. En este proyecto se utilizaron relaciones de uno a muchos y muchos a muchos, especialmente entre perfumes, marcas, colecciones, reseñas y carritos de compra. Gracias a esto se pudo entender cómo funcionan las conexiones entre tablas dentro de una base de datos relacional y cómo Django facilita mucho este proceso mediante código Python. El modelo Perfume fue una de las partes más completas del sistema, ya que integró imágenes, categorías, marcas, precios, stock y relaciones con otros modelos.

Otro aspecto importante fue la **creación y configuración del entorno de trabajo**. Durante el proyecto se aprendió a utilizar entornos virtuales, instalar librerías como Django y Pillow, ejecutar migraciones y trabajar con Git y GitHub para mantener actualizado el proyecto. Todo esto permitió comprender mejor cómo se organiza un proyecto real de desarrollo web y cómo deben administrarse sus dependencias y archivos.

Además, se logró entender la importancia de archivos fundamentales como `settings.py`, `urls.py`, `views.py` y `models.py`. El archivo `settings.py` funciona prácticamente como el **centro de control del proyecto**, ya que desde ahí se configura gran parte del comportamiento del sistema: las aplicaciones instaladas, la configuración de la base de datos SQLite, el manejo de archivos estáticos y multimedia, el modelo de usuario personalizado y diferentes configuraciones internas de Django.

El desarrollo de los templates `lista.html` y `detalle.html` permitió mejorar habilidades relacionadas con **HTML, CSS y templates de Django**. Gracias a estos archivos se logró crear una interfaz visual moderna y elegante para la perfumería virtual, utilizando diseños responsivos, tarjetas dinámicas, imágenes y estilos personalizados. Además, se aprendió a utilizar expresiones y estructuras condicionales de Django para mostrar información obtenida directamente desde la base de datos, lo cual hizo que el sitio web funcionara de manera dinámica.

Otro aprendizaje importante fue comprender el funcionamiento de las **migraciones en Django**. Mediante archivos como `0001_initial.py` se pudo observar cómo Django genera automáticamente la estructura de la base de datos a partir de los modelos creados en Python, sin necesidad de escribir manualmente código SQL complejo.

En cuanto al **funcionamiento CRUD**, el proyecto permitió practicar operaciones fundamentales dentro del desarrollo web — crear, consultar, modificar y eliminar registros — esenciales para prácticamente cualquier sistema moderno y que ayudaron a comprender cómo administrar información dentro de una aplicación web real.

Finalmente, este proyecto no solamente ayudó a fortalecer conocimientos técnicos, sino también habilidades relacionadas con organización, lógica de programación y estructura de proyectos. Se logró integrar programación backend, bases de datos, diseño visual y administración del sistema en una sola aplicación funcional. **PARFUMS** representó una experiencia muy completa para comprender el funcionamiento de Django y el desarrollo web moderno, permitiendo aplicar de forma práctica muchos de los conocimientos vistos durante el curso.

### Resumen de logros

| Área | Logro |
|------|-------|
| 🏗️ Arquitectura | MTV implementada correctamente |
| 🗄️ Base de datos | 7 modelos con relaciones 1:N y N:M |
| 🔐 Seguridad | UUIDs, usuario personalizado y validaciones |
| 🖥️ Interfaz | Templates elegantes con diseño oscuro y dorado |
| ⚙️ Admin | Panel con filtros, búsqueda, imágenes y totales dinámicos |
| 🛒 Carrito | Sistema completo con subtotales y total calculados |
| 🔄 CRUD | Operaciones completas desde el panel administrativo |
| 📦 Control de versiones | Proyecto publicado en GitHub con Git |

---

<div align="center">

**Perfumería Élite — PARFUMS**
*Tijuana, B.C. — 2026*

![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Powered%20by-Django-092E20?style=flat-square&logo=django&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Alxjandrz-181717?style=flat-square&logo=github&logoColor=white)

</div>

---

## 🏛️ Arquitectura del Sistema PARFUMS

El sistema PARFUMS fue desarrollado siguiendo la arquitectura **MTV (Model - Template - View)** de Django, la cual separa claramente las responsabilidades de cada componente del sistema:

| Capa | Archivo | Responsabilidad |
|------|---------|-----------------|
| **Model** | `models.py` | Define la estructura de la base de datos y las relaciones entre tablas |
| **Template** | `lista.html`, `detalle.html`, `carrito.html` | Interfaces visuales que muestran la información al usuario |
| **View** | `views.py` | Lógica del sistema que conecta modelos con templates |
| **URL** | `urls.py` | Enrutamiento de peticiones hacia las vistas correspondientes |

El flujo de una petición dentro del sistema es el siguiente:

```
Usuario → URL → View → Model → Base de datos
                  ↓
              Template → Respuesta visual al usuario
```

---

## 🔗 Relaciones de Base de Datos

El proyecto PARFUMS fue desarrollado utilizando una base de datos relacional mediante Django ORM y SQLite, permitiendo establecer conexiones eficientes entre los diferentes modelos del sistema. Estas relaciones fueron fundamentales para organizar correctamente la información de la perfumería y facilitar la interacción entre los datos.

### 🔷 Relaciones Uno a Muchos

Dentro del sistema se implementaron varias relaciones de uno a muchos, donde un registro principal puede relacionarse con múltiples registros secundarios.

#### Marca → Perfume
Una marca puede tener múltiples perfumes registrados dentro del sistema, mientras que cada perfume pertenece únicamente a una marca específica.

**Ejemplo:**
- Dior → Sauvage, Fahrenheit, Homme Intense
- Chanel → Bleu de Chanel, Allure Homme Sport

Esta relación se implementó mediante una `ForeignKey` dentro del modelo Perfume.

#### Perfume → Reseña
Cada perfume puede recibir muchas reseñas por parte de diferentes usuarios o clientes, mientras que cada reseña pertenece únicamente a un perfume.

Esto permite almacenar:
- Comentarios
- Calificaciones
- Fechas de publicación

para cada fragancia registrada.

#### User → Carrito
Un usuario puede tener múltiples carritos registrados en el sistema, mientras que cada carrito pertenece únicamente a un usuario específico. Esta relación se implementó mediante `ForeignKey` en el modelo Carrito apuntando al modelo User personalizado.

### 🔶 Relaciones Muchos a Muchos

También se implementaron relaciones de muchos a muchos para representar conexiones más complejas dentro del sistema.

#### Perfume ↔ Colección
Un perfume puede pertenecer a varias colecciones y, al mismo tiempo, una colección puede contener múltiples perfumes.

**Ejemplo:**
- Colección Verano → varios perfumes frescos
- Colección Nicho Exclusivo → perfumes de lujo seleccionados

Esta relación fue implementada utilizando `ManyToManyField` en Django ORM.

#### Perfume ↔ Carrito (via CarritoItem)
La relación entre perfumes y carritos se maneja mediante el modelo intermedio `CarritoItem`.

Esto permite:
- Agregar varios perfumes a un carrito
- Controlar cantidades
- Calcular subtotales
- Evitar productos repetidos

La tabla intermedia almacena información adicional necesaria para el funcionamiento del sistema de compras.

---

## ✅ Funcionamiento CRUD

El proyecto PARFUMS implementa operaciones CRUD completas utilizando el panel administrativo de Django y las herramientas proporcionadas por Django ORM.

CRUD representa las cuatro operaciones fundamentales utilizadas en cualquier sistema de gestión de datos:

### ➕ Create (Crear)

Permite registrar nueva información dentro de la base de datos. En el sistema se pueden crear:

- Perfumes
- Marcas
- Colecciones
- Reseñas
- Usuarios
- Carritos

Estas operaciones se realizan principalmente desde el panel administrativo de Django.

### 👁️ Read (Leer)

Permite consultar y visualizar información almacenada en la base de datos. Dentro del sistema los usuarios pueden:

- Visualizar el catálogo completo
- Consultar detalles de perfumes
- Revisar colecciones
- Observar reseñas
- Visualizar productos del carrito

Las consultas son realizadas mediante Django ORM utilizando métodos como:

```python
Perfume.objects.all()
Perfume.objects.filter(categoria='D')
get_object_or_404(Perfume, pk=pk)
```

### ✏️ Update (Actualizar)

Permite modificar registros existentes. Desde el panel administrativo se pueden actualizar:

- Precios
- Stock
- Imágenes
- Categorías
- Reseñas
- Información de marcas

### 🗑️ Delete (Eliminar)

Permite eliminar información almacenada en el sistema. Los administradores pueden eliminar:

- Perfumes
- Marcas
- Reseñas
- Colecciones
- Productos del carrito

Django administra automáticamente estas operaciones manteniendo la integridad de la base de datos.

| Operación | Panel Admin | Vista Pública | Descripción |
|-----------|-------------|---------------|-------------|
| ➕ **Create** | ✅ | ❌ | Agregar marcas, perfumes, colecciones, reseñas, carritos e ítems |
| 👁️ **Read** | ✅ | ✅ | Visualizar catálogo con filtros, búsqueda y detalle individual |
| ✏️ **Update** | ✅ | ❌ | Modificar cualquier campo de cualquier modelo |
| 🗑️ **Delete** | ✅ | ❌ | Eliminar registros con confirmación del sistema |

---

## 🗃️ Diseño de la Base de Datos

El diseño de la base de datos fue desarrollado siguiendo principios de organización, escalabilidad y normalización para garantizar un sistema eficiente y fácil de mantener.

### Modelos Principales

| Tabla | Campos principales | Relaciones |
|-------|-------------------|------------|
| `perfumes_user` | id (UUID), username, email, password, is_seller | → Carrito (1:N) |
| `perfumes_marca` | id (UUID), nombre, pais_origen | → Perfume (1:N) |
| `perfumes_perfume` | id (UUID), nombre, marca_id, precio, stock, ml, genero, categoria, imagen, imagen_url, en_stock, created_at | ← Marca, → Resena, ↔ Coleccion, ↔ CarritoItem |
| `perfumes_coleccion` | id (UUID), nombre, descripcion, fecha_inicio, fecha_fin | ↔ Perfume (N:M) |
| `perfumes_resena` | id (UUID), perfume_id, nombre_cliente, calificacion, comentario, fecha | ← Perfume |
| `perfumes_carrito` | id (UUID), user_id, created_at | ← User, ↔ Perfume via CarritoItem |
| `perfumes_carritoitem` | id (UUID), carrito_id, perfume_id, cantidad | ← Carrito, ← Perfume |
| `perfumes_coleccion_perfumes` | id, coleccion_id, perfume_id | Tabla intermedia automática N:M |

### Normalización

La base de datos fue organizada evitando redundancia de información mediante relaciones entre tablas. Esto permitió:

- Mejorar el rendimiento
- Reducir duplicidad de datos
- Facilitar mantenimiento
- Mantener integridad de la información

### Django ORM

El uso de Django ORM facilitó:

- Creación automática de tablas
- Manejo de relaciones
- Consultas dinámicas
- Migraciones automáticas
- Seguridad en consultas

Sin necesidad de escribir SQL manualmente en la mayoría del proyecto.

---

## 🖥️ Explicación del Panel Administrativo

El panel administrativo de Django (`/admin`) es el centro de gestión del sistema PARFUMS. Desde aquí se administran todos los modelos con funcionalidades avanzadas.

### 🧴 Artículos Carrito

En el apartado de **Artículos Carrito** es donde aparecen los artículos que han escogido los usuarios dentro de la página, mostrando de quién es el carrito, el perfume seleccionado, su precio, cantidad y la marca del perfume.

| Columna visible | Descripción |
|----------------|-------------|
| Perfume | Nombre de la fragancia seleccionada |
| Usuario | Propietario del carrito |
| Cantidad | Unidades seleccionadas |
| Subtotal | Precio calculado en tiempo real |
| Fecha pedido | Fecha de creación del carrito |

---

### 🛒 Carritos

Dentro del apartado **Carritos** es donde aparecen los carritos de todos los usuarios que han entrado y seleccionado productos en la página. Muestra el usuario propietario, la fecha de creación, el total de productos y el total monetario calculado automáticamente.

| Columna visible | Descripción |
|----------------|-------------|
| Usuario | Nombre del cliente |
| Fecha creación | Cuándo se creó el carrito |
| Productos | Cantidad de artículos distintos |
| Total | Suma total calculada en tiempo real |

Además, al entrar al detalle de un carrito, se pueden ver todos los productos que contiene gracias al **CarritoItemInline**, que muestra cada producto con su cantidad y subtotal directamente dentro del formulario.

---

### 🗂️ Colecciones

En el apartado de **Colecciones** es donde aparecen los perfumes de temporadas, para que el usuario pueda elegir dependiendo de sus necesidades. Se muestran las fechas en las que están activas las colecciones y el total de perfumes que contiene cada una.

El panel utiliza un **selector horizontal doble** (`filter_horizontal`) que permite asignar y remover perfumes de una colección de forma visual e intuitiva, sin necesidad de escribir nada manualmente.

---

### 🏷️ Marcas

Dentro del apartado **Marcas** es donde se agregan las marcas de los perfumes con su nombre y su país de origen. Incluye buscador por nombre y ordenamiento alfabático automático.

---

### 🌸 Perfumes

En el apartado **Perfumes** es donde se agregan los productos con toda su información: nombre, marca, precio, mililitros, género, categoría (Diseñador, Árabe, Nicho) e imagen del producto.

El panel de perfumes incluye funcionalidades avanzadas:

- 🔍 **Buscador** en tiempo real por nombre y marca
- 🔽 **Filtros laterales** por categoría, género, disponibilidad y marca
- 🖼️ **Vista previa de imagen** en miniatura dentro del listado
- 📋 **Fieldsets** que organizan los campos en secciones limpias
- 🗓️ **Fecha de registro** automática visible en modo solo lectura

---

### ⭐ Reseñas

En el apartado de **Reseñas** es donde los clientes pueden reseñar los perfumes y dejar sus referencias y experiencia propia de cómo les fue con el perfume, para que a la hora de comprarlo ya tengan una idea y puedan elegir mejor dependiendo sus gustos.

Tiene calificaciones del **1 al 5** para saber qué tan bueno es el perfume:

| Calificación | Significado |
|-------------|-------------|
| ⭐ 1 | Malo |
| ⭐⭐ 2 | Regular |
| ⭐⭐⭐ 3 | Bueno |
| ⭐⭐⭐⭐ 4 | Muy bueno |
| ⭐⭐⭐⭐⭐ 5 | Excelente |

El panel incluye filtros por calificación y por perfume, además de búsqueda por nombre de cliente, y se ordena por las más recientes primero.

---

## 🌐 Interfaz Pública del Catálogo

En el catálogo público (`/perfumes/`) aparecen todos los productos con todas sus especificaciones organizados en tres secciones: **Diseñador**, **Árabe** y **Nicho**, donde el usuario puede elegir el que desee o el que le parezca un buen obsequio.

### Vista de lista

Cada perfume se muestra como una tarjeta visual con:
- Imagen del producto
- Nombre y marca
- Mililitros y género
- Precio en MXN
- Indicador de disponibilidad

### Vista de detalle

Al dar clic en algún perfume, se muestra la información completa del producto. Si el perfume está disponible, aparece la opción de **Agregar al Carrito** con selector de cantidad. Al seguir bajando, el usuario puede dejar **reseñas** indicando qué tan bueno es el perfume según sus gustos personales, para guiar a otros compradores a tomar una mejor decisión.

### Vista del carrito

Al agregar un perfume al carrito, se muestra un resumen con:
- El perfume seleccionado
- Su precio unitario
- La cantidad seleccionada
- El subtotal por producto
- El **total general** calculado automáticamente


CAPTURAS DE ADMIN 

INICIO DEL ADMIN
<img width="1358" height="611" alt="articulos carritos" src="https://github.com/user-attachments/assets/38c562b5-e55d-43ff-b9e1-0188a0c360f2" />

ARTICULOS CARRITO
<img width="1365" height="613" alt="ART_CAR" src="https://github.com/user-attachments/assets/93f0e80e-33c5-4947-a369-6f201e050119" />

CARRITOS
<img width="684" height="356" alt="Carritos" src="https://github.com/user-attachments/assets/ee597682-4d6c-430b-a125-f358220892d0" />

COLECCIONES
<img width="668" height="374" alt="colecciones" src="https://github.com/user-attachments/assets/b5b94cd4-5bef-4b5c-bd4f-a0a437dceb27" />

MARCAS
<img width="664" height="344" alt="marcas_v1" src="https://github.com/user-attachments/assets/e76dae33-6907-4a7e-99e8-4eaf3cb92feb" />

<img width="694" height="369" alt="marcas_v2" src="https://github.com/user-attachments/assets/91813676-6a60-4fed-8661-b9963bcf5e06" />

<img width="657" height="337" alt="marcas_v3" src="https://github.com/user-attachments/assets/cb69d8d6-adf6-4423-b3e0-ec860c0ffdee" />

<img width="686" height="384" alt="marcas_v4" src="https://github.com/user-attachments/assets/a679dbc7-d56e-45f8-b5dd-a66812a380cb" />
 PERFUMES
<img width="649" height="397" alt="perfumes_v1" src="https://github.com/user-attachments/assets/4e5e53ad-e1ef-45c5-b77d-c320bb44cb17" />

<img width="617" height="390" alt="perfumes_v2" src="https://github.com/user-attachments/assets/1b75e01e-2bcb-4463-96a1-fa40c97d918a" />

<img width="632" height="429" alt="perfumes_v3" src="https://github.com/user-attachments/assets/7b2c7804-ee3e-4d7b-bbe0-190cb5a2a145" />

RESEÑAS
<img width="611" height="373" alt="reseñas_v1" src="https://github.com/user-attachments/assets/67ea9d8a-04ef-44ee-8674-6b2c63e67700" />

<img width="636" height="375" alt="reseñas_v2" src="https://github.com/user-attachments/assets/d1862f43-b6d4-4513-9c05-9507da3899d5" />


CAPTURAS PERFUMES(PROGRAMA EN EJECUCION)

<img width="607" height="363" alt="pantalla_1" src="https://github.com/user-attachments/assets/5fbc0453-a2e3-4600-9d9e-fc9f2078ef88" />

<img width="622" height="380" alt="pantalla_2" src="https://github.com/user-attachments/assets/f6a3c47a-fada-4c65-9c23-fd56b9173ee8" />

<img width="611" height="394" alt="pantalla_3" src="https://github.com/user-attachments/assets/869142b2-c1d7-4b03-bd82-97b94dc6d2b6" />

<img width="605" height="334" alt="pantalla_4" src="https://github.com/user-attachments/assets/219d9706-0c1c-4ae5-af2e-548e321c5c54" />

<img width="605" height="367" alt="pantalla_5" src="https://github.com/user-attachments/assets/f42ebf12-0feb-4bbd-bb95-1f49bb1de94a" />

<img width="555" height="366" alt="pantalla_6" src="https://github.com/user-attachments/assets/07c40541-5288-484e-aa80-5d1d5f0afc26" />

<img width="558" height="330" alt="pantalla_7" src="https://github.com/user-attachments/assets/f564c829-3de6-4863-812c-f4c2a1463cc7" />

<img width="562" height="296" alt="pantalla_8" src="https://github.com/user-attachments/assets/3ef34e3a-1a89-461b-bb3e-7e59a1345092" />

<img width="590" height="344" alt="pantalla_9" src="https://github.com/user-attachments/assets/c10051a7-4a3c-4388-ae92-2b999c4f3276" />

<img width="607" height="354" alt="pantalla_10" src="https://github.com/user-attachments/assets/07bf74f6-2c18-489c-a060-7c4d7616cb8a" />




















