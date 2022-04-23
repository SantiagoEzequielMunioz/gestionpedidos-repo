from django.contrib import admin

from shop.models import SeccionProducto,Producto

class SeccionAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(SeccionProducto,SeccionAdmin)
admin.site.register(Producto,ProductoAdmin)
