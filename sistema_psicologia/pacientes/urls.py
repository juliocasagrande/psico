from django.urls import path
from . import views

urlpatterns = [
    path('', views.paciente_lista, name='paciente_lista'),
    path('novo/', views.paciente_criar, name='paciente_criar'),
    path('editar/<int:pk>/', views.paciente_editar, name='paciente_editar'),
]