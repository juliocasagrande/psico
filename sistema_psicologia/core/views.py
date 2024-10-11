from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pacientes.models import Paciente
from evolucoes.models import Evolucao

@login_required
def home(request):
    return render(request, 'core/home.html')

def home(request):
    num_pacientes = Paciente.objects.count()
    num_evolucoes = Evolucao.objects.count()
    
    context = {
        'num_pacientes': num_pacientes,
        'num_evolucoes': num_evolucoes,
    }
    
    return render(request, 'core/home.html', context)