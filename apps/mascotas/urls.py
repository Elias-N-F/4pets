from django.urls import path
from . import views

app_name = "mascotas"

urlpatterns = [
	path("listar/", views.VerMascotas.as_view(), name="listar"),

	path("detalle/<int:pk>", views.DetallesMascota.as_view(), name="detalle"),
	
	path("nuevo/", views.RegistrarMascota.as_view(), name="nuevo"), 

	path("modificar/", views.ActualizarMascota.as_view(), name="modificar")

]
