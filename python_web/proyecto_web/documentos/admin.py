# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#-------------------------------

# Importar modelo 
from documentos.models import Documentos

#Crear sub-clase de admin.ModelAdmin
class DocumentoAdmin(admin.ModelAdmin):
	model = Documentos

#Registrar ModeloAdmin para cada modelo 
admin.site.register(Documentos, DocumentoAdmin)