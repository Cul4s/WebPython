#from django.contrib.auth.models import user

class Tarefa(models.Model):
    STATUS_CHOICES = [
      ('incompleta', "Incompleta!")
      ('andamemtp', "Em Andamento!")
      ('completa', "Realizada!")  
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criador = models.ForeignKey(User, related_name="minhas_tarefas", on_delete=models.CASCADE)
    responsavel = models.ForeignKey(User, related_name="tarefas_atribuidas", on_delete=models.CASCADE, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
   