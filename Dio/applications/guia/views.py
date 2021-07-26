

from django.shortcuts import render
from . models import guia
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

class ProductListView(ListView):
    template_name = "base_cliente/cliente.html"
    model = guia
    
   
    # def get_queryset(self):
    #     kword = self.request.GET.get("kword", '')
    #     order = self.request.GET.get("order", '')
    #     queryset = guia.objects.buscar_producto(kword, order)
    #     return queryset

class ProductDetailView(DetailView):
    template_name = "base_cliente/detail.html"
    model = guia