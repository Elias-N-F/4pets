from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mascota

class RegistrarMascota(LoginRequiredMixin, CreateView):
	model = Mascota
	template_name='pages/RegistroAnimalBasico.html'
	success_url = reverse_lazy("mascotas:listar")
	fields = ('imagen','nombre','edad','especie','raza','sexo','info_medica','veterinaria','dir_veterinaria')

class VerMascotas(LoginRequiredMixin,ListView):
	model = Mascota
	#template_name =
	def get_queryset(self):
		user= request.user
		context=Mascota.objects.filter(usuario=user)
		return context

class DetallesMascota(LoginRequiredMixin, DetailView):
	model = Mascota
	#template_name = 

class ActualizarMascota(LoginRequiredMixin, UpdateView):
	model = Mascota
	#template_name=
	fields = ('imagen','nombre','edad','especie','raza','sexo','info_medica','veterinaria','dir_veterinaria')