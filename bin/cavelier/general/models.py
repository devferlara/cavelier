from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField

# Create your models here.

class Generales(models.Model):
	nombre = models.CharField(max_length=80)
	logo_general = models.ImageField(upload_to='uploads', default='imagen/default.png')
	link_facebook = models.CharField(validators=[URLValidator()], max_length=100)
	link_twitter = models.CharField(validators=[URLValidator()], max_length=100)
	link_linkedn = models.CharField(validators=[URLValidator()], max_length=100)
	link_instagram = models.CharField(validators=[URLValidator()], max_length=100)
	fecha = models.DateTimeField(auto_now_add=True)
	union_logos = models.ImageField(upload_to='uploads', default='imagen/default.png')
	texto_bogota = RedactorField(verbose_name=u'Texto Bogota', default=' ')
	texto_medellin = RedactorField(verbose_name=u'Texto Medellin', default=' ')
	copyright = models.CharField(max_length=80, default=' ')

	def __unicode__(self):
		return self.nombre

class Areas_de_practica(models.Model):
	nombre = models.CharField(max_length=80)

	def __unicode__(self):
		return self.nombre

class Areas_de_practica_fr(models.Model):
	nombre = models.CharField(max_length=80)

	def __unicode__(self):
		return self.nombre	

class Areas_de_practica_en(models.Model):
	nombre = models.CharField(max_length=80)

	def __unicode__(self):
		return self.nombre

class Idiomas(models.Model):
	idioma = models.CharField(max_length=80)

	def __unicode__(self):
		return self.idioma

class Cargos(models.Model):
	cargo = models.CharField(max_length=80, default=' ')

	def __unicode__(self):
		return self.cargo

class Cargos_en(models.Model):
	cargo = models.CharField(max_length=80, default=' ')

	def __unicode__(self):
		return self.cargo

class Cargos_fr(models.Model):
	cargo = models.CharField(max_length=80, default=' ')

	def __unicode__(self):
		return self.cargo