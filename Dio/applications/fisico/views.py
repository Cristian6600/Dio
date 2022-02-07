from typing import List
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Paquete, Fisico
from django.views.generic import CreateView, ListView
from django.views.generic.detail import SingleObjectMixin
from .forms import ProductForm
from applications.users.mixins import CustodiaPermisoMixin

class BolsaCreateView(CustodiaPermisoMixin, CreateView, ListView):
    template_name = "fisico/add-fisico.html"
    form_class = ProductForm
    paginate_by = '5'
    success_url = '.'
    context_object_name = 'paquete'

    def get_queryset(self):
        return Paquete.objects.order_by('-fecha')

    def get_queryset(self):
        return Paquete.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(BolsaCreateView, self).form_valid(form)

class EstadoRutaListView(LoginRequiredMixin, ListView):
    template_name = "fisico/estado_ruta.html"
    queryset = Fisico.objects.filter(est_planilla = 1)
    paginate_by = 10
    success_url = '.'
    context_object_name ='estado_planilla'

