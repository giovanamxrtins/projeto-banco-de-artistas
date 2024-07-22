from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Infos_Artistas, Categoria
from .forms import CadastroArtista

def home(request):
    infos_artistas = Infos_Artistas.objects.all()
    form = CadastroArtista()
    return render(request, 'home.html', {'infos_artistas': infos_artistas, 'form': form})

def editar_artistas(request, id):
    infos_artistas = Infos_Artistas.objects.get(id = id)
    form = CadastroArtista()
    return render(request, 'editar_artistas.html', {'infos_artistas': infos_artistas, 'form': form, 'id_artista': id})

def cadastrar_artista(request):
    if request.method == 'POST':
        form = CadastroArtista(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('DADOS INVÁLIDOS')
        
def excluir_artista(request, id):
    artista = Infos_Artistas.objects.get(id = id).delete()
    return redirect('home')

def alterar_artista(request):
    artista_id = request.POST.get('artista_id')
    nome_artista = request.POST.get('nome_artista')
    email_artista = request.POST.get('email_artista')
    tipo_documento_artista = request.POST.get('tipo_documento_artista')
    documento_artista = request.POST.get('documento_artista')

    artista = Infos_Artistas.objects.get(id = artista_id)

    artista.nome = nome_artista
    artista.email = email_artista
    artista.tipo_documento = tipo_documento_artista
    artista.documento = documento_artista
    artista.save()
    return redirect(f'/info_artistas/editar_artistas/{artista_id}')