# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
# Create your views here.


def getDatoPeticion(request):
	identificador = request.GET.get("identificador")
	voltaje = request.GET.get("voltaje")
	uvindex = request.GET.get("uvindex")
	alerta = request.GET.get("alerta")

	dato = Dato()
	dato.identificador = identificador
	dato.voltaje = voltaje
	dato.uvindex = uvindex
	dato.alerta = alerta
	dato.llegado = datetime.datetime.now()
	dato.save()

	return HttpResponse(1)