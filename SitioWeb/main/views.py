from django.shortcuts import render
from carrito.carrito import Carro


def homepage(request):
    carro=Carro(request)
    return render(request,'base/homepage.html',{})



