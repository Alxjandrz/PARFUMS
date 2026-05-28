from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_perfumes, name='lista_perfumes'),
    path('<uuid:pk>/', views.detalle_perfume, name='detalle_perfume'),
    path('<uuid:pk>/agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('<uuid:pk>/resena/', views.agregar_resena, name='agregar_resena'), # <-- Nueva ruta
]