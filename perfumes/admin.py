from django.contrib import admin
from .models import Marca, Perfume, Coleccion, Resena, Carrito, CarritoItem


admin.site.register(Marca)
admin.site.register(Coleccion)
admin.site.register(Resena)
admin.site.register(Carrito)
admin.site.register(CarritoItem)


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'marca', 'precio', 'ml', 'genero', 'categoria', 'en_stock')

    list_filter = ('categoria', 'genero', 'en_stock', 'marca')

    search_fields = ('nombre', 'marca__nombre')