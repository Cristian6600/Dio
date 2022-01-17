
from typing import ContextManager
from django.db.models import fields
from django.db.models.query import QuerySet
from django.shortcuts import render
from applications.users.models import User
from applications.courrier.models import courrier
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.views.generic.dates import DayArchiveView

from django.contrib import messages

from django.utils import timezone
from django.views.generic.detail import DetailView

from django.core.paginator import Paginator
from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from .serializers import(
    CargueSerializer,
    FisicoSerializer
)

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

from django.views.generic import CreateView, View, ListView, UpdateView, DeleteView

from . models import Cargue,   Recepcion, Planilla

from .utils import render_to_pdf

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

from .forms import CargueForm
from .forms import RecepcionForm

#------------------Cargue----------------------------
class CargueCreateView( CreateView):
    template_name = "ruta_bootstrap/add_programador.html"
    form_class = CargueForm
    success_url = '.'
    context_object_name = 'coin_lst'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CargueCreateView, self).form_valid(form)

#----------------Recepcion------------------------

class RecepcionCreateView(CreateView, ListView ):
    # model= Recepcion
    # fields = ['planilla', 'motivo', 'estado', 'guia']
    template_name = "ruta/add-recepcion.html"
    form_class =  RecepcionForm
    initial = {'key':'value'}
    success_url = '.'
    paginate_by = '5'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recepcion Data Added')

        return render(request, self.template_name, {'form': form})

#------------------Pdf Cargue----------------------
class ListEmpleadosPdf(ListView):
    paginate_by = 2
    def get(self, request, *args, **kwargs):
        
        nombre = self.kwargs['full_name']
        
        mostrar_pla = Planilla.objects.latest('id')
        mostrar_nom = Planilla.objects.latest('cargue')
        mostrarpub = Planilla.objects.latest('fecha')
        guia = Planilla.objects.filter(cargue__id = nombre)
        data = {
            'count': guia.count(),
            'empleados': guia,
            'mostrarpub': mostrarpub,
            'mostrar_nom': mostrar_nom,
            'mostrar_pla': mostrar_pla
            
        }
        pdf = render_to_pdf('ruta/pdf_planillas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    def get_queryset(self):
            return ListEmpleadosPdf.objects.order_by('id')   
    
    
#-------------lista filtro planilla----------------------

class PLanillaListView(ListView): 
    template_name ='ruta/lista_planillas.html'
    context_object_name = 'lista'
    
    def get_queryset(self):

        nombre = self.kwargs['full_name']
        lista = Planilla.objects.filter(
        cargue__full_name = nombre
    )   
        return  lista
    
#---------------appi----------------------------
class FisicoListApiView(LoginRequiredMixin, ListAPIView):
    serializer_class = FisicoSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')

        return courrier.objects.filter(
            courrier__icontains =kword
        )

class RegistrarCargue(CreateAPIView):
    queryset = Cargue.objects.all()
    serializer_class = CargueSerializer
    permission_classes = [permissions.AllowAny]

#-------------lista filtro planilla----------------------
class PLanillaListView(ListView): 
    template_name ='ruta/lista_planillas.html'
    context_object_name = 'lista'
    
    def get_queryset(self):

        nombre = self.kwargs['id']
        lista = Planilla.objects.filter(
        cargue__id = nombre
    )   
        return  lista

#--------------busqueda por palabra clave------------
class ListPlanillasBykword(ListView):
    template_name = "ruta_bootstrap/add_programador.html"
    context_object_name = 'planillask'
    model = Cargue
    fields = ['__all__']
    ordering = '-id'
    paginate_by = '2'

    # def get_queryset(self):
    #     print('*************')
    #     palabra_clave = self.request.GET.get("kword",)
    #     lista = Cargue.objects.filter(
    #         id = palabra_clave
        
    # )  
        
    #     return lista
    

    