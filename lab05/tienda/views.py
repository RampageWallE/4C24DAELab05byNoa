from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tienda/lista_categorias.html', {'categorias': categorias})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tienda/lista_clientes.html', {'clientes': clientes})

def borrar_stock(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.stock = 0
        producto.save()

    return redirect(lista_productos)

def aumentar_stock_100u(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.stock += 100
        producto.save()

    return redirect(lista_productos)

def aumentar_precio_1sol(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.precio += 1
        producto.save()

    return redirect(lista_productos)
