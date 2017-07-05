# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.

#impoetar clase base para vista
#la vista manejan la logica de sitio web
from django.views.generic import View

 #metodo render retorna una respuesta 
 #combina una plantilla con un diccionario de contexto
 #y retorna un objeto HttResponse
from django.shortcuts import render
from documentos.models import Documentos as ModeloDocumentos

#Crear vista de documentos
#definir metodo get
class Documentos(View):
	def get(self, request, *args, **kwargs):
		docs = ModeloDocumentos.objects.all()
		context = {
		'docs': docs,
		'encabezado': 'Mis documentos'
		}
		return render ( 	
			request, 
			'documento.html', context)