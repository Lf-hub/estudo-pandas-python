from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(verbose_name=('Arquivo'), upload_to='files/')