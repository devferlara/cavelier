from django.shortcuts import render_to_response
from general.models import *
from contenido.models import *
from lineas_de_servicio.models import * 
from django.template import Context, RequestContext


def main(request):
	index = Pagina_principal.objects.all()
	return render_to_response("inicio.html", {'datos': index}, context_instance=RequestContext(request))

def cavelier_internacional(request):
	datos = Linea_de_servicio.objects.get(pk = 4)
	return render_to_response("cavelier_internacional.html", {'datos': datos}, context_instance=RequestContext(request))

def cavelier_propiedad(request):
	datos = Linea_de_servicio.objects.get(pk = 3)
	return render_to_response("cavelier_propiedad.html", {'datos': datos}, context_instance=RequestContext(request))

def cavelier_negocios(request):
	datos = Linea_de_servicio.objects.get(pk = 2)
	lineas = Linea_individual.objects.filter(linea=2)
	return render_to_response("cavelier_negocios.html", {'datos' : datos, 'lineas' : lineas}, context_instance=RequestContext(request))

def cavelier_litigios(request):
	datos = Linea_de_servicio.objects.get(pk = 1)
	return render_to_response("cavelier_litigios.html", {'datos': datos}, context_instance=RequestContext(request))

def cavelier_servicios(request, pks):
	datos = Linea_individual.objects.get(pk = pks)
	datos_imagen = Linea_de_servicio.objects.get(pk = datos.linea.pk)
	return render_to_response("cavelier_servicios.html", {'datos': datos, 'datos_imagen': datos_imagen}, context_instance=RequestContext(request))

