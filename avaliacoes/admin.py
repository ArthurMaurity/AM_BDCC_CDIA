from django.contrib import admin
from .models import Aluno, Avaliacao


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'ano', 'area', 'nota_tri', 'data_criacao')
    list_filter = ('ano', 'area')
