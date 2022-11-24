from django.contrib import admin
from .models import AlunoModel

class AdminAvaliacao(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'ano')
    search_fields = ('nome', 'curso', 'ano')

admin.site.register(AlunoModel)