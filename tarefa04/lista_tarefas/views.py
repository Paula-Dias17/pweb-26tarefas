from django.shortcuts import render
from datetime import date
from .models import Tarefas

def index(request):
    context = {
        'tarefas': Tarefas.objects.all(),
        'data_atual': date.today(),
    }
    return render(request, 'index.html', context)

