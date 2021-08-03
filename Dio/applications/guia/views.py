

from django.shortcuts import render
from . models import guia
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import guiafisicoForm
from . models import guia

class ProductListView(LoginRequiredMixin, ListView):
    template_name = "producto/cliente.html"
    model = guia
    paginate_by = 6
    success_url = '.'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = guia.objects.filter(
            Seudo__icontains=palabra_clave,
        )
        return lista
            
   
class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "producto/detail.html"
    model = guia

class bolsaCreateView(LoginRequiredMixin, CreateView):
    template_name = "guia/guia-fisico.html"
    model = guia
    form_class = guiafisicoForm
    success_url = '.'