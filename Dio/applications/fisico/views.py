from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import paquete
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.urls import reverse
from .forms import ProductForm



class bolsaCreateView(LoginRequiredMixin, CreateView):
    template_name = "fisico/add-fisico.html"
    model = paquete
    form_class = ProductForm
    success_url = '.'

class FisicoListView(LoginRequiredMixin, ListView):
    template_name = "fisico/ver-fisico.html"
    model = paquete
    paginate_by = 10
    success_url = '.'

