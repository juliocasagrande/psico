from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evolucao
from .forms import EvolucaoForm

@login_required
def evolucao_lista(request):
    query = request.GET.get('q')  # Captura o termo de busca da URL
    if query:
        evolucoes = Evolucao.objects.filter(paciente__nome__icontains=query)
    else:
        evolucoes = Evolucao.objects.all()
    
    return render(request, 'evolucoes/evolucao_lista.html', {'evolucoes': evolucoes})

@login_required
def evolucao_criar(request):
    if request.method == 'POST':
        form = EvolucaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evolucao_lista')
    else:
        form = EvolucaoForm()
    return render(request, 'evolucoes/evolucao_form.html', {'form': form})

@login_required
def evolucao_editar(request, pk):
    evolucao = get_object_or_404(Evolucao, pk=pk)
    if request.method == 'POST':
        form = EvolucaoForm(request.POST, instance=evolucao)
        if form.is_valid():
            form.save()
            return redirect('evolucao_lista')
    else:
        form = EvolucaoForm(instance=evolucao)
    return render(request, 'evolucoes/evolucao_form.html', {'form': form})

@login_required
def evolucao_detalhe(request, pk):
    evolucao = get_object_or_404(Evolucao, pk=pk)
    return render(request, 'evolucoes/evolucao_detalhe.html', {'evolucao': evolucao})

@login_required
def evolucao_ver(request, pk):
    evolucao = get_object_or_404(Evolucao, pk=pk)
    return render(request, 'evolucoes/evolucao_detalhe.html', {'evolucao': evolucao})
