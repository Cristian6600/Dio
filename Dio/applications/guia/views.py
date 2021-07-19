from django.shortcuts import render

from django.shortcuts import render
from . models import guia
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView

class ProductListView(ListView):
    template_name = "base_cliente/cliente.html"
    model = guia
    # context_object_name = 'lista'