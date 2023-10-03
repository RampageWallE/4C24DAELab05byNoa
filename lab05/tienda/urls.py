from django.urls import path 
from . import views

urlpatterns = [
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/aumentar/precio/1sol', views.aumentar_precio_1sol, name='aumentar_precio_1sol'),
    path('productos/aumentar/stock/100u',views.aumentar_stock_100u, name='aumentar_stock_100u' ),    
    path('productos/borrar/',views.borrar_stock, name='borrar_stock' ),
]