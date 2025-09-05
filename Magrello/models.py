from django.db import models

class Quadro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Lista(models.Model):
    nome = models.CharField(max_length=100)
    quadro = models.ForeignKey(Quadro, on_delete=models.CASCADE, related_name='listas')

    def __str__(self):
        return self.nome


class Cartao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='cartoes')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return self.titulo

