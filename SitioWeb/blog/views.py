from django.shortcuts import render
from blog.models import Post, Categoria

def blog(request):

    posteos = Post.objects.all()  
    return render(request,'blog/blog.html',{'posteos':posteos})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posteos = Post.objects.filter(categorias=categoria) #categorias es la variable ManyToManyField de la clase Post en views
    return render(request, 'blog/categoria.html',{'categoria':categoria,'posteos':posteos})

