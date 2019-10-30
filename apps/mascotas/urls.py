from django.urls import path
from . import views

app_name = "mascotas"

urlpatterns = [
	path("listar/", views.VerMascotas.as_view(), name="listMascota"),

	path("detalle/<int:pk>", views.DetallesMascota.as_view(), name="detailMascota"),
	
	path("nuevo/", views.RegistrarMascota.as_view(), name="newMascota"), 

	path("modificar/", views.ActualizarMascota.as_view(), name="updateMascota")

]
