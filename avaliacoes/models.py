from django.db import models


class Aluno(models.Model):
    """Um aluno cadastrado na plataforma Apollo."""

    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    """Uma avaliação (prova/simulado do ENEM) feita por um aluno."""

    AREA_CHOICES = [
        ('LC', 'Linguagens e Códigos'),
        ('CH', 'Ciências Humanas'),
        ('CN', 'Ciências da Natureza'),
        ('MT', 'Matemática'),
    ]

    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, related_name='avaliacoes'
    )
    ano = models.IntegerField(help_text='Edição do ENEM, ex.: 2025')
    area = models.CharField(max_length=2, choices=AREA_CHOICES)
    nota_tri = models.DecimalField(max_digits=6, decimal_places=1)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.aluno.nome} · ENEM {self.ano} · {self.area} · {self.nota_tri}'
