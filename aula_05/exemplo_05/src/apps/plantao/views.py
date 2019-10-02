from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Plantonista, Area
from .forms import PlantonistaForm


def home(request):
    return HttpResponse("<h1>Olá, mundo!</h1>")


def criar(request):
    formulário = PlantonistaForm(request.POST or None)
    if formulário.is_valid():
        formulário.save()
        return redirect('core:listar')
    return render(request, 'criar.html', {'form': formulário})


def listagem(request, id=None):
    dados = {}
    dados['plantonistas'] = Plantonista.objects.all()
    dados['areas'] = Area.objects.all()
    return render(request, 'listagem.html', dados)


def detalhes(request, id=None):
    queryset = get_object_or_404(Plantonista, id=id)
    contexto = {
        'coluna': queryset,
    }
    return render(request, "detalhes.html", contexto)


def alterar(request, id=None):
    queryset = Plantonista.objects.get(id=id)
    formulário = PlantonistaForm(request.POST or None, instance=queryset)
    if formulário.is_valid():
        formulário.save()
        return redirect('core:listar')
    contexto = {
        'coluna': queryset,
        'form': formulário
    }
    return render(request, 'alterar.html', contexto)


def deletar(request, id=None):
    queryset = Plantonista.objects.get(id=id)  # ou primary key, whatever
    if request.method == 'POST':
        queryset.delete()
        return redirect('core:listar')
    return render(request, 'deletar.html', {'coluna': queryset})
