from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Paquete
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views import View

from .forms import ProductForm

class BolsaCreateView(LoginRequiredMixin, CreateView):
    template_name = "fisico/add-fisico.html"
    form_class = ProductForm
    success_url = '.'

class FisicoListView(LoginRequiredMixin, ListView):
    template_name = "fisico/ver-fisico.html"
    model = Paquete
    paginate_by = 10
    success_url = '.'

# class FisicoCreateView(LoginRequiredMixin, CreateView):
#     template_name = "fisico/fisico.html"
#     form_class = FisicoForm
#     success_url = '.'

