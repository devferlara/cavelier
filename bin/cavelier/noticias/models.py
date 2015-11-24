from django.db import models
from redactor.fields import RedactorField

# Create your models here.

class Noticias_web(models.Model):
	nombre = models.CharField(max_length=400)
	fecha = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField(upload_to='photos')
	contenido = RedactorField(verbose_name=u'Contenido', default=' ')

	def __unicode__(self):
		return self.nombre
