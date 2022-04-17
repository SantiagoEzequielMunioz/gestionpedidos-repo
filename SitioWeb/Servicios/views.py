from django.shortcuts import render
from Servicios.models import Servicio

def services(request):

    servicios = Servicio.objects.all()  # con esto pido que importe todos los objetos en la clase servicios
    return render(request,'Servicios/services.html',{'servicios':servicios})
