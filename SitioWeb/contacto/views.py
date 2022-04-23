from django.shortcuts import redirect, render
from .forms import ContactoForm
from django.core.mail import EmailMessage

def contacto(request):

    formulario_contacto = ContactoForm()

    if request.method == 'POST':    #cuando toco enviar, en vez de usar el metodo GET, usa el POST
        formulario_contacto = ContactoForm(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            # preparamos mail // la lista de destinatarios pondria mi mail
            email = EmailMessage('Mensaje desde App Django',
            f'El usuario con nombre {nombre} con la direccion {email} escribe lo siguiente:\n\n {contenido}',
            '',['san88.zzl.308@gmail.com'],reply_to=[email])
    
            try:
                email.send()

                return redirect('/contacto/?valido')
            
            except:
                return redirect('/contacto/?no-valido')

    return render(request,'contacto/contacto.html',{'miform':formulario_contacto})

