from django.shortcuts import render
from blog.models import Post

def blog(request):

    posteos = Post.objects.all()  
    return render(request,'blog/blog.html',{'posteos':posteos})

