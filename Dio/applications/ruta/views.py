from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import (
    LenguajeSerializer,
    ProgramadorSerializer
)

from applications.fisico.models import Fisico

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

from django.views.generic import CreateView, View

from . models import Cargue, Planilla, Programador, Lenguaje

from .utils import render_to_pdf

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION


from .forms import CargueForm
from .forms import RecepcionForm

class CargueCreateView(LoginRequiredMixin, CreateView):
    template_name = "ruta/add-ruta.html"
    model = Cargue
    form_class = CargueForm
    success_url = '.'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CargueCreateView, self).form_valid(form)

class RecepcionCreateView(CreateView):
    template_name = "ruta/add-recepcion.html"
    form_class = RecepcionForm
    success_url = '.'

class ListEmpleadosPdf(View):
    
    def get(self, request, *args, **kwargs):
        empleados = Planilla.objects.all()
        data = {
            'count': empleados.count(),
            'empleados': empleados
        }
        pdf = render_to_pdf('ruta/empleados.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

"""  aqui empiezan los servicios """

class LenguajeListApiView(ListAPIView):
    serializer_class = LenguajeSerializer
    
    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')

        return Fisico.objects.filter(
            id_guia__icontains=kword
        )

class RegistrarProgramador(CreateAPIView):
    serializer_class = ProgramadorSerializer
