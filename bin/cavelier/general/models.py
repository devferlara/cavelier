from django.db import models
from django.core.validators import URLValidator
from redactor.fields import RedactorField

# Create your models here.

class generales(models.Model):
	nombre = models.CharField(max_length=80)
	logo_general = models.ImageField(upload_to='photos')
	link_facebook = models.CharField(validators=[URLValidator()], max_length=100)
	link_twitter = models.CharField(validators=[URLValidator()], max_length=100)
	link_linkedn = models.CharField(validators=[URLValidator()], max_length=100)
	link_instagram = models.CharField(validators=[URLValidator()], max_length=100)
	fecha = models.DateTimeField(auto_now_add=True)
	premio_logo_uno = models.ImageField(upload_to='photos', default='imagen/default.png')
	premio_logo_dos = models.ImageField(upload_to='photos', default='imagen/default.png')
	premio_logo_tres = models.ImageField(upload_to='photos', default='imagen/default.png')
	premio_logo_cuatro = models.ImageField(upload_to='photos', default='imagen/default.png')
	premio_logo_cinco = models.ImageField(upload_to='photos', default='imagen/default.png')
	premio_logo_seis = models.ImageField(upload_to='photos', default='imagen/default.png')
	union_logos = models.ImageField(upload_to='photos', default='imagen/default.png')
	texto_bogota = RedactorField(verbose_name=u'Texto Bogota', default=' ')
	texto_medellin = RedactorField(verbose_name=u'Texto Medellin', default=' ')
	copyright = models.CharField(max_length=80, default=' ')

	def __unicode__(self):
		return self.nombre