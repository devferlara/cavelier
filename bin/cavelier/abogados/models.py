from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField
from general.models import Areas_de_practica, Idiomas, Cargos

class Abogado_individual(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	fecha = models.DateTimeField(auto_now_add=True)
	lema = models.CharField(max_length=200, default=' ')
	imagen = models.ImageField(upload_to='uploads', default='imagen/default.png')
	mail = models.CharField(max_length=100, default=' ')
	telefonos = models.CharField(max_length=100, default=' ')
	telefono_directo = models.CharField(max_length=100, default=' ')
	formacion = RedactorField(verbose_name=u'Formacion academica', default=' ')
	experiencia = RedactorField(verbose_name=u'Experiencia Laboral', default=' ')
	Publicaciones = RedactorField(verbose_name=u'Publicaciones', default=' ')
	idiomas = models.ManyToManyField(Idiomas, blank=True)
	cargo = models.ManyToManyField(Cargos, blank=True, null=True)
	areas_practica = models.ManyToManyField(Areas_de_practica, blank=True)

	def __unicode__(self):
		return self.nombre

