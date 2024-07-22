from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('editar_artistas/<int:id>', views.editar_artistas, name = 'editar_artistas'),
    path('cadastrar_artista', views.cadastrar_artista, name='cadastrar_artista'),
    path('excluir_artista/<int:id>', views.excluir_artista, name='excluir_artista'),
    path('alterar_artista', views.alterar_artista, name="alterar_artista")
]