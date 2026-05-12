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
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    ml = models.IntegerField(help_text="Mililitros")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    notas_olfativas = models.TextField(blank=True)
    en_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"