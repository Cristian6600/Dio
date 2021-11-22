
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import guiafisicoForm
from . models import Guia


class ProductListView(LoginRequiredMixin, ListView):
    template_name = "producto/cliente.html"
    model = Guia
    paginate_by = 5
    success_url = '.'
    # page_kwarg = 'page'
           
class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "producto/detail.html"
    model = Guia

class bolsaCreateView(CreateView):
    template_name = "guia/guia-fisico.html"
    form_class = guiafisicoForm
    success_url = '.'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(bolsaCreateView, self).form_valid(form)

    

    
