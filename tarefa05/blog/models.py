from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='imgs/')
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo

