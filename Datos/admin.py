# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class DatoAdmin(admin.ModelAdmin):
	list_display = ('identificador', 'voltaje', 'uvindex', 'alerta', 'llegado','temperatura', 'ciudad', 'latitud', 'longitud',)

admin.site.register(Dato, DatoAdmin)
