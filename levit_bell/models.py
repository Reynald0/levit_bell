from django.db import models

class Tip(models.Model):
	titulo = models.CharField(max_lenght=60)
	texto = models.TextField()

