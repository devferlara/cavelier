from django.conf import settings
from general.models import Generales

def current_site(request):
    try:
        current_site = Generales.objects.all()
        return {
            'current_site': {'var': current_site[0]},
        }
    except Generales.DoesNotExist:

        return {'current_site':{'var':'Juanito'}} # an empty string