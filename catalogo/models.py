from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub Categoria'
        verbose_name_plural = 'Sub Categorias'
