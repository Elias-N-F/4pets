from django import forms
from .models import Mascota
from django_superform import SuperModelForm

class MascotasForm(SuperModelForm ,forms.Form):


	class Meta:
		model = Mascota
		fields = ('imagen','nombre','fec_nac','especie','raza','sexo','nomb_opcional')

