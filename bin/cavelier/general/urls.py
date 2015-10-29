from django.conf.urls import include, url, patterns
from .views import main

urlpatterns = patterns ('',
	#Pagina principal
	url(r'^$', 'general.views.main'),
	url(r'^(?P<name>\w+)/inicio/', 'general.views.main'),

	#Lineas de servicios
	url(r'^cavelier_internacional/', 'general.views.cavelier_internacional'),
	url(r'^cavelier_propiedad_intelectual/', 'general.views.cavelier_propiedad'),
	url(r'^cavelier_negocios/', 'general.views.cavelier_negocios'),
	url(r'^cavelier_litigios/', 'general.views.cavelier_litigios'),

	url(r'^servicio/(\d+)/$', 'general.views.cavelier_servicios'),

)

