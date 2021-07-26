from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from . models import Fisico
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.urls import reverse



class InventarioCreateView(CreateView):
    template_name = "fisico/add-fisico.html"
    context_object_name = 'Inventario'
    model = Fisico
    fields = ['Bolsa', 'Seudo']
    success_url = '.'