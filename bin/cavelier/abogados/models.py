from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField
from general.models import *

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

	formacion_ingles = RedactorField(verbose_name=u'Formacion academica Ingles', default=' ')
	experiencia_ingles = RedactorField(verbose_name=u'Experiencia Laboral Ingles', default=' ')
	Publicaciones_ingles = RedactorField(verbose_name=u'Publicaciones Ingles', default=' ')

	formacion_frances = RedactorField(verbose_name=u'Formacion academica Frances', default=' ')
	experiencia_frances = RedactorField(verbose_name=u'Experiencia Laboral Frances', default=' ')
	Publicaciones_frances = RedactorField(verbose_name=u'Publicaciones Frances', default=' ')

	idiomas = models.ManyToManyField(Idiomas, blank=True)
	cargo = models.ManyToManyField(Cargos, blank=True, null=True)
	cargo_en = models.ManyToManyField(Cargos_en, blank=True, null=True)
	cargo_fr = models.ManyToManyField(Cargos_fr, blank=True, null=True)

	areas_practica = models.ManyToManyField(Areas_de_practica, blank=True)
	areas_practica_ingles = models.ManyToManyField(Areas_de_practica_en, blank=True)
	areas_practica_frances = models.ManyToManyField(Areas_de_practica_fr, blank=True)

	def __unicode__(self):
		return self.nombre

