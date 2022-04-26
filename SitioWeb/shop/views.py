from django.shortcuts import render
from .models import Producto

def shop(request):
    
    productos = Producto.objects.all()

    return render(request,'shop/shop.html',{'productos':productos})
