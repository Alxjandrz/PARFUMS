from django.shortcuts import render, get_object_or_404
from .models import Perfume, Coleccion, Resena


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
    return render(request, 'perfumes/detalle.html', {
        'perfume': perfume,
        'resenas': resenas,
        'colecciones': colecciones,
    })