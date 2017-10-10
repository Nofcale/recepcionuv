# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dato(models.Model):
	identificador = models.CharField(verbose_name='ID', max_length=50)
	voltaje = models.CharField(verbose_name='Voltaje', max_length=50)
	uvindex = models.CharField(verbose_name='UV Index', max_length=50)
	alerta = models.CharField(verbose_name='Alerta', max_length=50)
	llegado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora de recepción')

	def __unicode__(self):
		return self.identificador