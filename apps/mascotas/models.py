from django.db import models
from apps.users.models import CustomUser as User

# Create your models here.


class InfoMedica(models.Model):
	info_medica=models.TextField(max_length=200)
	nom_doc=models.CharField(max_length=30, null=True, blank=True)
	nom_vet=models.CharField(max_length=20, null=True, blank=True)
	dir_vet=models.CharField(max_length=35, null=True, blank=True)
	tel_vet=models.CharField(max_length=10, null=True, blank=True)
	cp_vet=models.CharField(max_length=4, null=True, blank=True)
	ciudad_vet=models.CharField(max_length=15, null=True, blank=True)
	detalles_vet=models.CharField(max_length=200, null=True, blank=True)

class Mascota(models.Model):

	usuario= models.ForeignKey(User, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to = 'mascotas')
	nombre = models.CharField(max_length=30)
	nomb_opcional=models.CharField(max_length=30, blank=True, null=True)
	especie=models.CharField(max_length=20,)
	raza= models.CharField(max_length=20,null = True, blank=True)
	sexo= models.CharField(max_length=15,)
	fec_nac=models.DateField()
	existe=models.BooleanField(default=True)
	
	class Meta():
		unique_together=('usuario','nombre')

	def __str__(self):
		return self.nombre
