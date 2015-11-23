from django.shortcuts import render_to_response
from general.models import *
from contenido.models import *
from lineas_de_servicio.models import * 
from abogados.models import *
from firma.models import *
from django.template import Context, RequestContext


#Pagina principal
def main(request, name):
	index = Pagina_principal.objects.all()

	if name=='':
		idioma = 'ESP'
	else:
		idioma = name

	response = render_to_response("inicio.html", {'datos': index, 'idioma': idioma}, context_instance=RequestContext(request))
	return response

def main_sin_argumento(request):
	index = Pagina_principal.objects.all()
	idioma = 'ESP'
	response = render_to_response("inicio.html", {'datos': index, 'idioma': idioma}, context_instance=RequestContext(request))
	return response
#Pagina principal

#Lineas de servicio
def cavelier_internacional(request, name):
	datos = Linea_de_servicio.objects.get(pk = 4)
	return render_to_response("cavelier_internacional.html", {'datos': datos, 'idioma': name}, context_instance=RequestContext(request))

def cavelier_propiedad(request, name):
	datos = Linea_de_servicio.objects.get(pk = 3)
	return render_to_response("cavelier_propiedad.html", {'datos': datos, 'idioma': name}, context_instance=RequestContext(request))

def cavelier_negocios(request, name):
	datos = Linea_de_servicio.objects.get(pk = 2)
	lineas = Linea_individual.objects.filter(linea=2)
	return render_to_response("cavelier_negocios.html", {'datos' : datos, 'lineas' : lineas, 'idioma': name}, context_instance=RequestContext(request))

def cavelier_litigios(request, name):
	datos = Linea_de_servicio.objects.get(pk = 1)
	return render_to_response("cavelier_litigios.html", {'datos': datos, 'idioma': name}, context_instance=RequestContext(request))

def cavelier_servicios(request, pks):
	datos = Linea_individual.objects.get(pk = pks)
	datos_imagen = Linea_de_servicio.objects.get(pk = datos.linea.pk)
	return render_to_response("cavelier_servicios.html", {'datos': datos, 'datos_imagen': datos_imagen, 'idioma': 'es'}, context_instance=RequestContext(request))
def cavelier_servicios_en(request, pks):
	datos = Linea_individual.objects.get(pk = pks)
	datos_imagen = Linea_de_servicio.objects.get(pk = datos.linea.pk)
	return render_to_response("cavelier_servicios.html", {'datos': datos, 'datos_imagen': datos_imagen, 'idioma': 'en'}, context_instance=RequestContext(request))
def cavelier_servicios_fr(request, pks):
	datos = Linea_individual.objects.get(pk = pks)
	datos_imagen = Linea_de_servicio.objects.get(pk = datos.linea.pk)
	return render_to_response("cavelier_servicios.html", {'datos': datos, 'datos_imagen': datos_imagen, 'idioma': 'fr'}, context_instance=RequestContext(request))
#Lineas de servicio



#Listar areas
def cavelier_areas(request, name):

	if name == 'es':
		index = Areas_de_practica.objects.all()
		idioma = name
	elif name == 'en':
		index = Areas_de_practica_en.objects.all()
		idioma = name
	elif name == 'fr':
		index = Areas_de_practica_fr.objects.all()
		idioma = name
	else:
		index = Areas_de_practica.objects.all()
		idioma = 'es'
	
	response = render_to_response("cavelier_areas_de_practica.html", {'datos': index, 'idioma': idioma}, context_instance=RequestContext(request))
	return response

#Abogados por area  

def abogados_por_area(request, name, id):

	if name == 'es':
		index = Abogado_individual.objects.filter(areas_practica=id)
		idioma = name
	elif name == 'en':
		index = Abogado_individual.objects.filter(areas_practica_ingles=id)
		idioma = name
	elif name == 'fr':
		index = Abogado_individual.objects.filter(areas_practica_frances=id)
		idioma = name
	else:
		index = Abogado_individual.objects.filter(areas_practica=id)
		idioma = name

	response = render_to_response("cavelier_abogados_por_area.html", {'datos': index, 'idioma': idioma}, context_instance=RequestContext(request))
	return response

def abogado(request, name, id):
	index = Abogado_individual.objects.filter(pk=id) 
	idioma = name
	response = render_to_response("abogado_individual.html", {'datos': index, 'idioma': idioma}, context_instance=RequestContext(request))
	return response

def abogados_alfabetica(request, name):
	index = Abogado_individual.objects.all().order_by('apellidos')
	response = render_to_response("todos_abogados.html", {'datos': index, 'idioma': name}, context_instance=RequestContext(request))
	return response

def acerca_firma(request, name):
	datos = acerca.objects.get(pk=1)
	if name == 'es':
		contenido = datos.texto_descripcion
	elif name == 'en':
		contenido = datos.texto_descripcion_en
	elif name == 'fr':
		contenido = datos.texto_descripcion_fr
	else:
		contenido = datos.texto_descripcion

	response = render_to_response("cavelier_firma_acerca.html", {'datos': datos, 'contenido': contenido, 'idioma': name}, context_instance=RequestContext(request))
	return response


def conducta_firma(request, name):
	datos = conducta.objects.get(pk=1)
	if name == 'es':
		contenido = datos.texto_descripcion
	elif name == 'en':
		contenido = datos.texto_descripcion_en
	elif name == 'fr':
		contenido = datos.texto_descripcion_fr
	else:
		contenido = datos.texto_descripcion

	response = render_to_response("cavelier_firma_conducta.html", {'datos': datos, 'contenido': contenido, 'idioma': name}, context_instance=RequestContext(request))
	return response



def reconocimientos_firma(request, name):
	datos = reconocimientos.objects.get(pk=1)
	if name == 'es':
		contenido = datos.texto_descripcion
	elif name == 'en':
		contenido = datos.texto_descripcion_en
	elif name == 'fr':
		contenido = datos.texto_descripcion_fr
	else:
		contenido = datos.texto_descripcion

	response = render_to_response("cavelier_firma_reconocimientos.html", {'datos': datos, 'contenido': contenido, 'idioma': name}, context_instance=RequestContext(request))
	return response


def membresias_firma(request, name):
	datos = membresias.objects.get(pk=1)
	if name == 'es':
		contenido = datos.texto_descripcion
	elif name == 'en':
		contenido = datos.texto_descripcion_en
	elif name == 'fr':
		contenido = datos.texto_descripcion_fr
	else:
		contenido = datos.texto_descripcion

	response = render_to_response("cavelier_firma_membresias.html", {'datos': datos, 'contenido': contenido, 'idioma': name}, context_instance=RequestContext(request))
	return response


def lineas(request, name):
	datos = Linea_general.objects.get(pk=1)

	response = render_to_response("cavelier_linea_general.html", {'datos': datos, 'idioma': name}, context_instance=RequestContext(request))
	return response

def trabaje(request, name):
	datos = Trabaje_con_nosotros.objects.get(pk=1)
	response = render_to_response("cavelier_trabaje.html", {'datos': datos, 'idioma': name}, context_instance=RequestContext(request))
	return response
