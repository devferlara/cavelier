from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField

# Create your models here.

class Linea_de_servicio(models.Model):
	nombre = models.CharField(max_length=80)
	imagen = models.ImageField(upload_to='uploads', default='imagen/default.png')
	imagen_interna = models.ImageField(upload_to='uploads', default='imagen/default.png')
	texto_lema = RedactorField(verbose_name=u'Lema', default=' ')
	texto_descripcion = RedactorField(verbose_name=u'Descripcion', default=' ')

	def __unicode__(self):
		return self.nombre

class Linea_individual(models.Model):
	nombre = models.CharField(max_length=100)
	linea = models.ForeignKey(Linea_de_servicio, blank=True, default='')
	contenido = RedactorField(verbose_name=u'Descripcion', default=' ')

	def __unicode__(self):
		return self.nombre + u" --- " + self.linea.nombre