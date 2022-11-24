from django.shortcuts import render
from .models import AlunoModel
from .forms import AlunoForm
# Create your views here.

def retorna_alunos(request):
    return render(request, 'alunos.html')

def cadastro(request):
    if request.method == "GET":
        form = AlunoForm()
        context = {"form": form}
        return render(request, 'cadastro.html', context)
    else:
        form = AlunoForm(request.POST)
        if form.is_valid():
            AlunoModel.objects.create(**form.cleaned_data) 
            context = {"form": form}
            return render(request, 'alunos.html', context)
        else:
            context = {"form": form}
            return render(request, 'cadastro.html', context)

def index(request):
    return render(request, 'index.html')
    