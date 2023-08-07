from typing import Any
from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(verbose_name=('Arquivo'), upload_to='files/')

class Lines(models.Model):
    contest = models.IntegerField(verbose_name='Concurso')
    content_json = models.JSONField(verbose_name='Conteúdo')

    class Meta:
        verbose_name = "Concurso"

    def __str__(self):
        return f'{self.contest}'