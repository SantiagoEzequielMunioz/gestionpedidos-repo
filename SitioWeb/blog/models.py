from django.db import models

from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'  #este nombre va a tener en el panel de admin si es uno
        verbose_name_plural = 'categorias' #este nombre va a tener en el panel de admin si son varios
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog',null=True, blank=True)  #null me saca la obligatoriedad de poner imagen, y blank me rellena
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)  # categorias la uso para el filtrado
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posteos'
    
    def __str__(self):
        return self.titulo