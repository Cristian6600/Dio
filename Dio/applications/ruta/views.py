from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView

from . models import Cargue

from .forms import CargueForm
from .forms import RecepcionForm

class CargueCreateView(CreateView):
    template_name = "ruta/add-ruta.html"
    model = Cargue
    form_class = CargueForm
    success_url = '.'

class RecepcionCreateView(CreateView):
    template_name = "ruta/add-recepcion.html"
    model = Cargue
    form_class = RecepcionForm
    success_url = '.'