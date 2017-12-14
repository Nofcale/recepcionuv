# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import *
# Register your models here.

class AdminExport(ImportExportActionModelAdmin):
    pass

admin.site.register(Dato, AdminExport)