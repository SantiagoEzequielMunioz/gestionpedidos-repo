from django.shortcuts import render
from .forms import ContactoForm

def contacto(request):

    formulario_contacto = ContactoForm()

    return render(request,'contacto/contacto.html',{'miform':formulario_contacto})

