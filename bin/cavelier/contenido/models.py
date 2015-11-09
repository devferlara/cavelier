from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField

# Create your models here.

class Pagina_principal(models.Model):
	nombre = models.CharField(max_length=80)
	fecha = models.DateTimeField(auto_now_add=True)
	imagen_slide = models.ImageField(upload_to='uploads', default='imagen/default.png')
	imagen_slide_en = models.ImageField(upload_to='uploads', default='imagen/default.png', blank=True)
	imagen_slide_fr = models.ImageField(upload_to='uploads', default='imagen/default.png', blank=True)
	iimagen_litigios = models.ImageField(upload_to='uploads', default='imagen/default.png')
	imagen_negocios = models.ImageField(upload_to='uploads', default='imagen/default.png')
	imagen_propiedad = models.ImageField(upload_to='uploads', default='imagen/default.png')
	imagen_internacional = models.ImageField(upload_to='uploads', default='imagen/default.png')
	imagen_video = models.ImageField(upload_to='uploads', default='imagen/default.png')
	imagen_articulos = models.ImageField(upload_to='uploads', default='imagen/default.png')
	premio_logo_uno = models.ImageField(upload_to='uploads', default='imagen/default.png')
	premio_logo_dos = models.ImageField(upload_to='uploads', default='imagen/default.png')
	premio_logo_tres = models.ImageField(upload_to='uploads', default='imagen/default.png')
	premio_logo_cuatro = models.ImageField(upload_to='uploads', default='imagen/default.png')
	premio_logo_cinco = models.ImageField(upload_to='uploads', default='imagen/default.png')
	premio_logo_seis = models.ImageField(upload_to='uploads', default='imagen/default.png')


	def __unicode__(self):
		return self.nombre