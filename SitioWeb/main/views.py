from django.shortcuts import render


def homepage(request):
    return render(request,'base/homepage.html',{})

def shop(request):
    return render(request,'base/shop.html',{})

def blog(request):
    return render(request,'base/blog.html',{})

def contact(request):
    return render(request,'base/contact.html',{})