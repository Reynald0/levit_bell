from django.db import models
from django.utils import timezone

class Tip(models.Model):
	titulo = models.CharField(max_length=60)
	texto = models.TextField()
	fecha_publicacion = models.DateTimeField(blank=True, null = True)

#	def publicar(self):
#		self.fecha_publicacion = timezone.now()
#		self.save()
#
#
#	def __str__(self):
#   	return self.titulo
