from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request,'registro/registro.html',{'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            #si el form es válido, lo guardo
            usuario = form.save()
            #una vez que se crea el usuario, se logea automaticamente a mi sitio
            #hago un login automatico
            login(request,usuario)
            #una vez logeado, redirijo a home
            return redirect('home')
        else:
            #con esto recorro todos los errores que haya en el array
            for msg in form.error_messages:
                #muestro el mensaje que corresponda
                messages.error(request,form.error_messages[msg])
            
            return render(request,'registro/registro.html',{'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def logear(request):

    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            #asigno una variable con lo que el usuario completó en el campo 'username'
            #con el get rescato la info del campo 'username' y 'password'
            nombre_user = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=nombre_user,password=contra)
            if user is not None:    # si hay algo...
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Usuario no válido')
        else:
            messages.error(request,'Información incorrecta')

    form = AuthenticationForm()
    return render(request,'login/login.html',{'form':form})
