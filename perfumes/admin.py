from django.contrib import admin
from django.utils.html import format_html
from .models import User, Marca, Perfume, Coleccion, Resena, Carrito, CarritoItem


# =========================
# Marca
# =========================
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen')
    search_fields = ('nombre', 'pais_origen')
    ordering = ('nombre',)


# =========================
# Perfume
# =========================
@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio', 'ml', 'genero', 'categoria', 'en_stock', 'ver_imagen')
    list_filter = ('categoria', 'genero', 'en_stock', 'marca')
    search_fields = ('nombre', 'marca__nombre')
    ordering = ('nombre',)
    readonly_fields = ('ver_imagen_detalle', 'created_at')

    fieldsets = (
        ('Informacion general', {
            'fields': ('nombre', 'marca', 'categoria', 'genero')
        }),
        ('Precio y stock', {
            'fields': ('precio', 'stock', 'ml', 'en_stock')
        }),
        ('Descripcion', {
            'fields': ('notas_olfativas',)
        }),
        ('Imagen', {
            'fields': ('imagen', 'ver_imagen_detalle', 'imagen_url')
        }),
        ('Fecha de registro', {
            'fields': ('created_at',)
        }),
    )

    def ver_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:contain;"/>', obj.imagen.url)
        elif obj.imagen_url:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:contain;"/>', obj.imagen_url)
        return 'Sin imagen'
    ver_imagen.short_description = 'Imagen'

    def ver_imagen_detalle(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="200" style="object-fit:contain;"/>', obj.imagen.url)
        elif obj.imagen_url:
            return format_html('<img src="{}" width="200" style="object-fit:contain;"/>', obj.imagen_url)
        return 'Sin imagen'
    ver_imagen_detalle.short_description = 'Vista previa'


# =========================
# Coleccion
# =========================
@admin.register(Coleccion)
class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'total_perfumes')
    search_fields = ('nombre',)
    filter_horizontal = ('perfumes',)
    ordering = ('nombre',)

    def total_perfumes(self, obj):
        return obj.perfumes.count()
    total_perfumes.short_description = 'Total perfumes'


# =========================
# Resena
# =========================
@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'perfume', 'calificacion', 'fecha')
    list_filter = ('calificacion', 'perfume')
    search_fields = ('nombre_cliente', 'perfume__nombre')
    ordering = ('-fecha',)


# =========================
# CarritoItem dentro de Carrito
# =========================
class CarritoItemInline(admin.TabularInline):
    model = CarritoItem
    extra = 1
    readonly_fields = ('subtotal',)
    fields = ('perfume', 'cantidad', 'subtotal')


# =========================
# Carrito
# =========================
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_items', 'total_carrito')
    search_fields = ('user__username',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    inlines = [CarritoItemInline]

    def total_items(self, obj):
        return obj.carritoitem_set.count()
    total_items.short_description = 'Productos'

    def total_carrito(self, obj):
        return f"${obj.total}"
    total_carrito.short_description = 'Total'


# =========================
# CarritoItem independiente
# =========================
@admin.register(CarritoItem)
class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('perfume', 'get_usuario', 'cantidad', 'subtotal', 'get_fecha')
    search_fields = ('perfume__nombre', 'carrito__user__username')
    list_filter = ('carrito__user',)
    ordering = ('-carrito__created_at',)

    def get_usuario(self, obj):
        return obj.carrito.user.username
    get_usuario.short_description = 'Usuario'

    def get_fecha(self, obj):
        return obj.carrito.created_at
    get_fecha.short_description = 'Fecha pedido'

