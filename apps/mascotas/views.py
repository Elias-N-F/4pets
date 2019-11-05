from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mascota
from .forms import MascotasForm
from django.http import HttpResponse, HttpResponseRedirect

class RegistrarMascota(LoginRequiredMixin, CreateView):
	model = Mascota
	template_name='pages/RegistroAnimalBasico.html'
	success_url = reverse_lazy("mascotas:listar")
	form_class=MascotasForm

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		us=request.user
		form.usuario=us
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		print(form)
		print(type(form))

		#request= HttpResponseRedirect(reverse("mascotas:nuevo2",form1=form))
		#return request
	def form_invalid(self,form):
		print("conchetumare")

		request= HttpResponse("nope")
		return request

def RegistrarParte2(request, form1):
	print(form1)

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