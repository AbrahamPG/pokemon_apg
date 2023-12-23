from django.db import models

# Create your models here.
class Catalog(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    pais = models.CharField(max_length=27, default='')

    def __str__(self):
        return "{}, {}".format(self.nombre, self.pais)