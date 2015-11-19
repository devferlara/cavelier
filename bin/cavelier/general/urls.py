from django.conf.urls import include, url, patterns
from .views import main

urlpatterns = patterns ('',
	#Pagina principal
	url(r'^$', 'general.views.main_sin_argumento'),

	url(r'^(?P<name>\w+)/inicio/', 'general.views.main'),

	#Lineas de servicios
	url(r'^(?P<name>\w+)/cavelier_internacional/', 'general.views.cavelier_internacional'),
	url(r'^(?P<name>\w+)/cavelier_propiedad_intelectual/', 'general.views.cavelier_propiedad'),
	url(r'^(?P<name>\w+)/cavelier_negocios/', 'general.views.cavelier_negocios'),
	url(r'^(?P<name>\w+)/cavelier_litigios/', 'general.views.cavelier_litigios'),

	#Cavelier servicios individuales
	url(r'^es/servicio/(\d+)/$', 'general.views.cavelier_servicios'),
	url(r'^en/servicio/(\d+)/$', 'general.views.cavelier_servicios_en'),
	url(r'^fr/servicio/(\d+)/$', 'general.views.cavelier_servicios_fr'),

	#cavelier lista de areas dependiendo el idioma
	url(r'^(?P<name>\w+)/areas-de-practica/', 'general.views.cavelier_areas'),

	#lista de abogados segun area e idioma
	url(r'^(?P<name>\w+)/area/(?P<id>\w+)/$', 'general.views.abogados_por_area'),

	#lista de todos los abogados alfabeticamente
	url(r'^(?P<name>\w+)/abogados-az/$', 'general.views.abogados_alfabetica'),

	#abogado ver
	url(r'^(?P<name>\w+)/abogado/(?P<id>\w+)/$', 'general.views.abogado'),

	#seccion firma
	url(r'^(?P<name>\w+)/firma/acerca/$', 'general.views.acerca_firma'),

)

