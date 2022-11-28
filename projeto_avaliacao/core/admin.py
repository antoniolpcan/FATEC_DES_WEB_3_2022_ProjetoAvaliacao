from django.contrib import admin
from .models import AlunoModel, Palestra

class AdminAvaliacao(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'ano')
    search_fields = ('nome', 'curso', 'ano')

class AdminAvaliacao(admin.ModelAdmin):
    list_display = ('palestra', 'palestrantes', 'curriculo', 'dia_hora', 'sala' )
    search_fields = ('palestra', 'palestrantes', 'curriculo', 'dia_hora', 'sala' )

admin.site.register(AlunoModel)
admin.site.register(Palestra)