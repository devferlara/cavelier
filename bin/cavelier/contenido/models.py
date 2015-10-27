from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField

# Create your models here.

class pagina_principal(models.Model):
	nombre = models.CharField(max_length=80)
	fecha = models.DateTimeField(auto_now_add=True)
	imagen_slide = models.ImageField(upload_to='photos')
	imagen_litigios = models.ImageField(upload_to='photos')
	imagen_negocios = models.ImageField(upload_to='photos')
	imagen_propiedad_intelectual = models.ImageField(upload_to='photos')
	imagen_internacional = models.ImageField(upload_to='photos')
	imagen_video = models.ImageField(upload_to='photos')
	imagen_articulos = models.ImageField(upload_to='photos')

	def __unicode__(self):
		return self.nombre