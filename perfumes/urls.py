from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_perfumes, name='lista_perfumes'),
    path('<int:pk>/', views.detalle_perfume, name='detalle_perfume'),
]