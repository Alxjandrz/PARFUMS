from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfume, Coleccion, Resena, Carrito, CarritoItem

def lista_perfumes(request):
    disenador = Perfume.objects.filter(categoria='D')
    arabes = Perfume.objects.filter(categoria='A')
    nicho = Perfume.objects.filter(categoria='N')
    return render(request, 'perfumes/lista.html', {
        'disenador': disenador,
        'arabes': arabes,
        'nicho': nicho,
    })

def detalle_perfume(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    resenas = perfume.resenas.all().order_by('-fecha')
    colecciones = perfume.colecciones.all()
    
    # Intentamos obtener el carrito del usuario si está autenticado para el contador superior
    carrito = None
    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(user=request.user)

    return render(request, 'perfumes/detalle.html', {
        'perfume': perfume,
        'resenas': resenas,
        'colecciones': colecciones,
        'carrito': carrito,
    })

# ==========================================
# GESTIÓN DE CARRITO
# ==========================================

@login_required
def agregar_al_carrito(request, pk):
    if request.method == 'POST':
        perfume = get_object_or_404(Perfume, pk=pk)
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
    return render(request, 'perfumes/carrito.html', {
        'carrito': carrito
    })

# ==========================================
# NUEVA VISTA PARA AGREGAR RESEÑAS
# ==========================================

def agregar_resena(request, pk):
    if request.method == 'POST':
        perfume = get_object_or_404(Perfume, pk=pk)
        nombre_cliente = request.POST.get('nombre_cliente', '').strip()
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario', '').strip()

        # Validación simple para asegurar que los datos no vayan vacíos
        if nombre_cliente and calificacion and comentario:
            Resena.objects.create(
                perfume=perfume,
                nombre_cliente=nombre_cliente,
                calificacion=int(calificacion),
                comentario=comentario
            )
            
    return redirect('detalle_perfume', pk=pk)