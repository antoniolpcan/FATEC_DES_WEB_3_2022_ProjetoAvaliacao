from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cadastro', views.cadastro),
    path('alunos', views.retorna_alunos),
]