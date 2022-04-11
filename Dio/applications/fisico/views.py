from dataclasses import field
from typing import List
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Cobertura, Paquete, Fisico, Bolsa
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from .forms import ProductForm, CoberturaForm
from applications.users.mixins import CustodiaPermisoMixin
from applications.courrier.models import courrier
from django.contrib import messages
from simple_history.models import HistoricalRecords

class BolsaCreateView(CustodiaPermisoMixin, CreateView, ListView):
    template_name = "fisico/add-fisico.html"
    form_class = ProductForm
    paginate_by = '5'
    success_url = '.'
    context_object_name = 'paquete'

    # def get_queryset(self):
    #     return Paquete.objects.order_by('-fecha')

    def get_queryset(self):
        return Paquete.objects.filter(user=self.request.user).order_by('-fecha')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(BolsaCreateView, self).form_valid(form)

class EstadoRutaListView(LoginRequiredMixin, ListView):
    template_name = "fisico/estado_ruta.html"
    model = Fisico
    queryset = Fisico.objects.filter(est_planilla = 1)
    paginate_by = 5
    context_object_name ='estado_planilla'

    # def get_queryset(self):
    #     kword = self.request.GET.get("kword", '')
    #     order = self.request.GET.get("order", '')
    #     queryset = courrier.objects.buscar_producto(kword, order)
    #     return queryset

class CoberturaCreateView(CreateView, ListView):
    template_name = "fisico/cobertura_bolsa.html"
    form_class = CoberturaForm
    # context_object_name = 'cobertura'
    success_url = '.'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Planilla Data Added')

        return render(request, self.template_name, {'form': form})

    def get_queryset(self):
        return Cobertura.objects.order_by('bolsa')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CoberturaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto ['lista_cobertura'] = self.get_queryset()
        contexto ['form'] = self.form_class
        
        return contexto


class Bolsa_add_CreateView(CreateView, ListView):
    model = Bolsa
    fields =['bolsa',]
    template_name = "fisico/create_bolsa.html"
    success_url = '.'   

    def get_queryset(self):
        return Bolsa.objects.order_by('-fecha_bolsa')[:5]



        

        