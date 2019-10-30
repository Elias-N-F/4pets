from django.db import models
from apps.users.models import CustomUser as User

# Create your models here.
class Mascota(models.Model):

	OTRO='OT'

	#Selecciones de sexo
	MACHO='MA'
	HEMBRA='HE'
	ELEGIR_SEXO=[(MACHO,'Macho'),(HEMBRA,'Hembra'),(OTRO,'Otro')]

	#Selecciones de especie
	PERRO='PE'
	GATO='GA'
	ROEDOR='RO'
	PAJARO='PA'
	ANFIBIO='AN'
	ELEGIR_ESPECIE=[(PERRO,'Perro'),
	(GATO,'Gato'),
	(ROEDOR,'Roedor (Conejos, Hamsters, etc.)'),
	(PAJARO,'Pajaro'),
	(ANFIBIO,'Anfibio'),
	(OTRO,'Otro')]

	usuario= models.ForeignKey(User, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to = 'mascotas')
	nombre = models.CharField(max_length=30)
	edad = models.DecimalField(max_digits= 3, decimal_places=0)
	especie=models.CharField(max_length=2,choices=ELEGIR_ESPECIE,default=OTRO)
	raza= models.CharField(max_length=20,null = True, blank=True)
	sexo= models.CharField(max_length=2,choices=ELEGIR_SEXO,default=OTRO)
	info_medica=models.TextField(max_length=200)
	veterinaria=models.CharField(max_length=20,null = True, blank=True)
	dir_veterinaria=models.CharField(max_length=35)
	existe=models.BooleanField(default=True)
	#lo de la id usamos la id de la db nomas o generamos una nosotros?


	class Meta():
		unique_together=('usuario','nombre')

	def __str__(self):
		return self.nombre