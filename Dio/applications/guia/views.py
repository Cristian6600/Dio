

from django.shortcuts import render
from . models import guia
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

class ProductListView(LoginRequiredMixin, ListView):
    template_name = "producto/cliente.html"
    model = guia
    
   
    # def get_queryset(self):
    #     kword = self.request.GET.get("kword", '')
    #     order = self.request.GET.get("order", '')
    #     queryset = guia.objects.buscar_producto(kword, order)
    #     return queryset

class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "producto/detail.html"
    model = guia