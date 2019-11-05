from django.contrib import admin
from .models import Mascota, InfoMedica
# Register your models here.



#registrame en el sitio del admin, mi MODELO
admin.site.register(Mascota)
admin.site.register(InfoMedica)