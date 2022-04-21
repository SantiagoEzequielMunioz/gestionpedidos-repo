from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    # los parametros se colocan entre <param>, este param. llama a ese id de la db
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]