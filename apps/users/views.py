from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import CustomUser

class Registrarte(CreateView):
	model = CustomUser
	fields =('name','lastname','email','username','residence','password')
	template_name='us/pages/RegistroPersona.html'
	success_url = reverse_lazy("mascotas:listar")
	
