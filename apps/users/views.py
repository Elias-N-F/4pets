from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import CustomUser
from .forms import CustomUserCreationForm

class Registrarte(CreateView):
	model = CustomUser
	form_class=CustomUserCreationForm
	template_name='pages/RegistroPersona.html'
	success_url = reverse_lazy("mascotas:listar")
	def form_invalid(self, form):
		
		return self.render_to_response(self.get_context_data(form=form))