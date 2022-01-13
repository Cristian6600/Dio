from typing import List
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Paquete
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views import View

from .forms import ProductForm

class BolsaCreateView(LoginRequiredMixin, CreateView, ListView):
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

class FisicoListView(LoginRequiredMixin, ListView):
    template_name = "fisico/ver-fisico.html"
    model = Paquete
    paginate_by = 10
    success_url = '.'

# class FisicoCreateView(LoginRequiredMixin, CreateView):
#     template_name = "fisico/fisico.html"
#     form_class = FisicoForm
#     success_url = '.'

