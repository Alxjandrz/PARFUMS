from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Perfume(models.Model):
    GENERO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('U', 'Unisex'),
    ]
    CATEGORIA_CHOICES = [
        ('D', 'Diseñador'),
        ('A', 'Árabe'),
    ]
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    ml = models.IntegerField(help_text="Mililitros")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, default='D')
    notas_olfativas = models.TextField(blank=True)
    en_stock = models.BooleanField(default=True)
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"

class Coleccion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    perfumes = models.ManyToManyField(Perfume, related_name='colecciones', blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Resena(models.Model):
    CALIFICACION_CHOICES = [
        (1, '1 - Malo'),
        (2, '2 - Regular'),
        (3, '3 - Bueno'),
        (4, '4 - Muy bueno'),
        (5, '5 - Excelente'),
    ]
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE, related_name='resenas')
    nombre_cliente = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=CALIFICACION_CHOICES)
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_cliente} — {self.perfume.nombre} ({self.calificacion}★)"