from django.urls import path
from .views import VRegistro,cerrar_sesion,logear


urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),
    path('logout', cerrar_sesion, name='logout'),
    path('logear', logear, name='logear'),
]
