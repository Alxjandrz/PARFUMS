from django.shortcuts import render, get_object_or_404
from .models import Perfume, Marca

def lista_perfumes(request):
    disenador = Perfume.objects.filter(categoria='D')
    arabes = Perfume.objects.filter(categoria='A')
    return render(request, 'perfumes/lista.html', {
        'disenador': disenador,
        'arabes': arabes,
    })

def detalle_perfume(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    return render(request, 'perfumes/detalle.html', {'perfume': perfume})