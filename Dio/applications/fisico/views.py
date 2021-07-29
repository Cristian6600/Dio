from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Fisico, paquete
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.urls import reverse
from .forms import ProductForm, FisicoForm


class InventarioCreateView(LoginRequiredMixin, CreateView):
    template_name = "fisico/add-fisico.html"
    
    model = Fisico
    form_class = FisicoForm
    success_url = '.'

class bolsaCreateView(LoginRequiredMixin, CreateView):
    template_name = "fisico/fisico.html"
    form_class = ProductForm
    success_url = '.'