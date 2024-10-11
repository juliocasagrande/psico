from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm

@login_required
def paciente_lista(request):
    search_query = request.GET.get('search', '')  # Captura o termo de busca, se existir
    if search_query:
        pacientes = Paciente.objects.filter(nome__icontains=search_query)  # Filtra por nome
    else:
        pacientes = Paciente.objects.all()  # Mostra todos os pacientes se não houver busca
    return render(request, 'pacientes/paciente_lista.html', {'pacientes': pacientes, 'search_query': search_query})

@login_required
def paciente_criar(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_lista')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/paciente_form.html', {'form': form})

@login_required
def paciente_editar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_lista')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/paciente_form.html', {'form': form})