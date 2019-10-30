from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

	name = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	residence = models.CharField(max_length=40)
	#username=CharField(max_length=1, null=True,blank=True)
	email = models.EmailField(unique=True)
	
	gender= models.CharField(max_length=10,)
	image = models.ImageField(upload_to = 'userimages',null= True,blank=True)

	#USERNAME_FIELD='email'
	#REQUIRED_FIELDS=['name','lastname','residence','gender']

	#IMPORTANTE!!! De ser necesario agregar el parametro
	#uploadto... Ej:
	#(upload_to='niperraidea', null= True)
