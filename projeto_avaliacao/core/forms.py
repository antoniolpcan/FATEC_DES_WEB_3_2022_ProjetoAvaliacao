from django import forms 

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=50, error_messages={"invalid": "Nome inválido."})
    curso = forms.CharField(max_length=50, error_messages={"invalid": "Curso inválido."})
    ano = forms.IntegerField(error_messages={"invalid": "Ano inválido."})

