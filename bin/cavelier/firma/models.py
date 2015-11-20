from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField

class acerca(models.Model):
	nombre = models.CharField(max_length=80)
	texto_descripcion = RedactorField(verbose_name=u'Contenido', default=' ')
	texto_descripcion_en = RedactorField(verbose_name=u'Contenido Ingles', default=' ')
	texto_descripcion_fr = RedactorField(verbose_name=u'Contenido Frances', default=' ')
	imagen_interna = models.ImageField(upload_to='uploads', default='imagen/default.png')

	def __unicode__(self):
		return self.nombre


class conducta(models.Model):
	nombre = models.CharField(max_length=80)
	texto_descripcion = RedactorField(verbose_name=u'Contenido', default=' ')
	texto_descripcion_en = RedactorField(verbose_name=u'Contenido Ingles', default=' ')
	texto_descripcion_fr = RedactorField(verbose_name=u'Contenido Frances', default=' ')
	imagen_interna = models.ImageField(upload_to='uploads', default='imagen/default.png')

	def __unicode__(self):
		return self.nombre


class reconocimientos(models.Model):
	nombre = models.CharField(max_length=80)
	texto_descripcion = RedactorField(verbose_name=u'Contenido', default=' ')
	texto_descripcion_en = RedactorField(verbose_name=u'Contenido Ingles', default=' ')
	texto_descripcion_fr = RedactorField(verbose_name=u'Contenido Frances', default=' ')
	imagen_interna = models.ImageField(upload_to='uploads', default='imagen/default.png')

	def __unicode__(self):
		return self.nombre


class membresias(models.Model):
	nombre = models.CharField(max_length=80)
	texto_descripcion = RedactorField(verbose_name=u'Contenido', default=' ')
	texto_descripcion_en = RedactorField(verbose_name=u'Contenido Ingles', default=' ')
	texto_descripcion_fr = RedactorField(verbose_name=u'Contenido Frances', default=' ')
	imagen_interna = models.ImageField(upload_to='uploads', default='imagen/default.png')

	def __unicode__(self):
		return self.nombre
