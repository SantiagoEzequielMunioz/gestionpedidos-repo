from django.db import models



class SeccionProducto(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Seccion'
        verbose_name_plural = 'Secciones'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='shop',null=True,blank=True)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    seccion = models.ManyToManyField(SeccionProducto)
    # si fuera una relacion Uno a Muchos iria con la siguiente instruccion
    # seccion = models.ForeignKey(SeccionProducto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre



