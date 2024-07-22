from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length = 10)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Infos_Artistas(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.CharField(max_length = 50)
    documento = models.CharField(max_length = 11)
    tipo_documento = models.CharField(max_length = 3)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Info Artista'