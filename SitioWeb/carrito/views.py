from django.shortcuts import render

from .carrito import Carro
from shop.models import Producto
from django.shortcuts import redirect

def agregar_producto(request,producto_id):
    # primero creo el objeto
    carro = Carro(request)
    # en un query en la db busco el id del mismo con el ingresado en el objeto
    # lo meto todo en la variable prod
    prod=Producto.objects.get(id=producto_id)
    
    carro.agregar(producto=prod)

    return redirect('shop')

def eliminar_producto(request,producto_id):
    
    carro = Carro(request)
    prod=Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=prod)

    return redirect('shop')

def restar_producto(request,producto_id):
    
    carro = Carro(request)
    prod=Producto.objects.get(id=producto_id)
    
    carro.restar_producto(producto=prod)

    return redirect('shop')

def limpiar_carro(request,producto_id):
    
    carro = Carro(request)
        
    carro.limpiar_carro()

    return redirect('shop')