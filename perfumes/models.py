import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# =========================
# Usuario
# =========================
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# =========================
# Marca — Uno a Muchos con Perfume
# =========================
class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# =========================
# Perfume — Muchos a Uno con Marca
# =========================
class Perfume(models.Model):
    GENERO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('U', 'Unisex'),
    ]
    CATEGORIA_CHOICES = [
        ('D', 'Disenador'),
        ('A', 'Arabe'),
        ('N', 'Nicho'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        related_name='perfumes'
    )
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


# =========================
# Coleccion — Muchos a Muchos con Perfume
# =========================
class Coleccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    perfumes = models.ManyToManyField(
        Perfume,
        related_name='colecciones',
        blank=True
    )
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre


# =========================
# Resena — Muchos a Uno con Perfume
# =========================
class Resena(models.Model):
    CALIFICACION_CHOICES = [
        (1, '1 - Malo'),
        (2, '2 - Regular'),
        (3, '3 - Bueno'),
        (4, '4 - Muy bueno'),
        (5, '5 - Excelente'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    nombre_cliente = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=CALIFICACION_CHOICES)
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.perfume.nombre} ({self.calificacion})"


# =========================
# Carrito — Uno a Muchos con Usuario
# =========================
class Carrito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carritos'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.user.username}"

    @property
    def total(self):
        # CORREGIDO: Se cambia 'carritoitem_set' por 'items'
        return sum(item.subtotal for item in self.items.all())


# =========================
# CarritoItem — Tabla intermedia Muchos a Muchos
# =========================
class CarritoItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE,
        related_name='items'
    )
    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE,
        related_name='carrito_items'
    )
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('carrito', 'perfume')

    @property
    def subtotal(self):
        return self.perfume.precio * self.cantidad

    def __str__(self):
        return f"{self.perfume.nombre} x {self.cantidad} — {self.carrito.user.username}"