# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import *
# Register your models here.
class DatoAdmin(ImportExportActionModelAdmin):
	list_display = ('identificador', 'voltaje', 'uvindex', 'alerta', 'llegado','temperatura', 'ciudad', 'latitud', 'longitud',)

admin.site.register(Dato, DatoAdmin)
