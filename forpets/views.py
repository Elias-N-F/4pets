from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse, HttpResponseRedirect, Http404

class Home(TemplateView):
	template_name='HomePage.html'
