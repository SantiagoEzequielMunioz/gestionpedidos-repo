from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request,'registro/registro.html',{'form':form})

    def post(self, request):
        pass


# def autenticacion(request):

#     if request.method == 'POST':
#         form = UserCreationForm()
#         if form.is_valid():
#             form.save()
#         else:

#     else:
#         form = {}
#     return render(request, 'registro/registro.html',{'form':form})

