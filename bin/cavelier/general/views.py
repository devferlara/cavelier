from django.shortcuts import render_to_response
from general.models import Generales
from contenido.models import Pagina_principal
from django.template import Context, RequestContext


def main(request):
	gen = Generales.objects.all()
	index = Pagina_principal.objects.all()

	return render_to_response("inicio.html", {'datos': index}, context_instance=RequestContext(request))