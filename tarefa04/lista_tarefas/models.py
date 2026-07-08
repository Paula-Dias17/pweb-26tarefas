from django.db import models

class Tarefas(models.Model):
    nome = models.CharField(max_length=20)
    status = models.BooleanField()
    prazo = models.DateField()

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        if self.status:
            status = "Tarefa realizada"
            
        else: 
            status="Tarefa não realizada"

        return (f"Nome: {self.nome} | Status: {status} | Prazo: {self.prazo}")

