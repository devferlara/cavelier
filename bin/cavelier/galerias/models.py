from django.db import models

# Create your models here.

class galerias(models.Model):
	imagen = models.ImageField(upload_to='uploads', default='imagen/default.png')

	def __unicode__(self):
		return self.imagen