from django.shortcuts import render
from .models import AlunoModel, Palestra
from .forms import AlunoForm

def retorna_alunos(request):
    alunos_all = AlunoModel.objects.all()
    alunos = {"alunos": alunos_all}
    return render(request, 'alunos.html', alunos)

def cadastro(request):
    form = AlunoForm()
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            AlunoModel.objects.create(**form.cleaned_data) 
            form = AlunoForm()
            context = {"form": form}
            return render(request, 'cadastro.html', context)
        else:
            context = {"form": form}
            return render(request, 'cadastro.html', context)
    else:
        form = AlunoForm()
        context = {"form": form}
        return render(request, 'cadastro.html', context)

def index(request):
    palestras_all = Palestra.objects.all()
    palestras = {"palestras": palestras_all}
    return render(request, 'index.html', palestras)
    