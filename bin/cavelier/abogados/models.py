from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField
from general.models import areas_de_practica, idiomas

class abogado_individual(models.Model):
	nombre = models.CharField(max_length=100)
	fecha = models.DateTimeField(auto_now_add=True)
	lema = models.CharField(max_length=200)
	imagen = models.ImageField(upload_to='photos', default='imagen/default.png')
	idiomas = models.ManyToManyField(idiomas, blank=True)

	areas_practica = models.ManyToManyField(areas_de_practica, blank=True)
	

	def __unicode__(self):
		return self.nombre

