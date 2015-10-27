from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField
from general.models import areas_de_practica, idiomas, cargos

class abogado_individual(models.Model):
	nombre = models.CharField(max_length=100)
	fecha = models.DateTimeField(auto_now_add=True)
	lema = models.CharField(max_length=200, default=' ')
	imagen = models.ImageField(upload_to='photos', default='imagen/default.png')
	mail = models.CharField(max_length=100, default=' ')
	telefonos = models.CharField(max_length=100, default=' ')
	telefono_directo = models.CharField(max_length=100, default=' ')
	formacion = RedactorField(verbose_name=u'Formacion academica', default=' ')
	experiencia = RedactorField(verbose_name=u'Experiencia Laboral', default=' ')
	Publicaciones = RedactorField(verbose_name=u'Publicaciones', default=' ')
	idiomas = models.ManyToManyField(idiomas, blank=True)
	cargo = models.OneToOneField(cargos, blank=True, null=True)
	areas_practica = models.ManyToManyField(areas_de_practica, blank=True)

	def __unicode__(self):
		return self.nombre

