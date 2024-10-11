from django.urls import path
from . import views

urlpatterns = [
    path('', views.evolucao_lista, name='evolucao_lista'),
    path('nova/', views.evolucao_criar, name='evolucao_criar'),
    path('detalhe/<int:pk>/', views.evolucao_detalhe, name='evolucao_detalhe'),
    path('<int:pk>/editar/', views.evolucao_editar, name='evolucao_editar'),
]