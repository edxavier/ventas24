from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import *
from catalogo.models import *

# Create your models here.

class Publicacion(models.Model):
    sub_categoria = models.ForeignKey(SubCategoria)
    titulo = models.CharField(max_length=160)
    descripcion = models.TextField()
    intencion = models.CharField(max_length=30)
    precio = IntegerRangeField()
    negociable = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    prioridad = models.IntegerField(default=0)

    tags = ArrayField(models.CharField(max_length=50), default=["venta", "compras"])
    contacto = JSONField(default={'eder':'eder'})
    datos = JSONField(default={}, blank=True, null=True)

    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
