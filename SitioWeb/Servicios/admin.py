from django.contrib import admin
from .models import Servicio   # el . indica que se mueve en el mismo directorio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio, ServicioAdmin)   
