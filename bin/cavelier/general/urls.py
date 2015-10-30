from django.conf.urls import include, url, patterns
from .views import main

urlpatterns = patterns ('',
	#Pagina principal
	url(r'^$', 'general.views.main_sin_argumento'),

	url(r'^(?P<name>\w+)/inicio/', 'general.views.main'),

	#Lineas de servicios
	url(r'^cavelier_internacional/', 'general.views.cavelier_internacional'),
	url(r'^cavelier_propiedad_intelectual/', 'general.views.cavelier_propiedad'),
	url(r'^cavelier_negocios/', 'general.views.cavelier_negocios'),
	url(r'^cavelier_litigios/', 'general.views.cavelier_litigios'),

	#Cavelier servicios individuales
	url(r'^servicio/(\d+)/$', 'general.views.cavelier_servicios'),

	#cavelier lista de areas dependiendo el idioma
	url(r'^(?P<name>\w+)/areas-de-practica/', 'general.views.cavelier_areas'),

	#lista de abogados segun area e idioma
	url(r'^(?P<name>\w+)/area/(?P<id>\w+)/$', 'general.views.abogados_por_area'),

	#abogado ver
	url(r'^(?P<name>\w+)/abogado/(?P<id>\w+)/$', 'general.views.abogado'),

)

