from django.db import models

class PontoTuristico(models.Model):
    nome      = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado  = models.BooleanField(default=False)

    # Definir o nome plural da minha classe
    class Meta:
        verbose_name_plural = 'PontosTuristicos'
    
    # Definir o campo default
    def __str__(self):
        return self.nome
