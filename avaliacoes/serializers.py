from rest_framework import serializers
from .models import Aluno, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'aluno', 'ano', 'area', 'nota_tri', 'data_criacao']


class AlunoSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'avaliacoes']
