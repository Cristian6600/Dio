
from re import template
from typing import ContextManager
from django.db.models import fields
from django.db.models.query import QuerySet
from django.shortcuts import render
from applications.users.models import User
from applications.guia.models import Guia
from applications.courrier.models import courrier
from django.views.generic.dates import DayArchiveView
from django.db.models import Q

from applications.guia.models import Guia

from django.contrib import messages

from applications.users.mixins import CustodiaPermisoMixin

from django.contrib.auth.decorators import login_required, permission_required

from django.core.paginator import Paginator
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

from django.views.generic import CreateView, ListView, View

from . models import Planilla, Descargue, Recepcion, Destino

from .utils import render_to_pdf

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

from .forms import CargueForm, RecepcionForm, AsignarForm, DestinoForm, DescargueForm

#----------------Recepcion------------------------
class RecepcioCreateView(CustodiaPermisoMixin, CreateView, ListView ):
       
    template_name = "ruta/add-recepcion.html"
    form_class = RecepcionForm
    initial = {'key':'value'}
    success_url = '.'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(RecepcioCreateView, self).form_valid(form)
        
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
class ListEmpleadosPdf(CustodiaPermisoMixin, ListView):

    def get(self, request, *args, **kwargs):
        
        nombre = self.kwargs['full_name']
               
        mostrar_nom = Guia.objects.filter(mensajero__id = nombre, est_planilla = 1).order_by('fecha_planilla')[0]
        mostrarpub = Guia.objects.latest('fecha')
        guia = Guia.objects.filter(mensajero__id = nombre, est_planilla = 1 ).order_by('fecha_planilla')
        data = {
            'count': guia.count(),
            'empleados': guia,
            'mostrarpub': mostrarpub,
            'mostrar_nom': mostrar_nom
                                    
        }
        pdf = render_to_pdf('ruta/pdf_planillas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
    #------------------Asignar guia a mensajero--------------------

class AsignarCreateView(CreateView, ListView):
    template_name = "ruta/asignar.html"
    form_class = AsignarForm
    queryset = Planilla.objects.order_by('-fecha')
    initial = {'key':'value'}
    paginate_by = '5'
    
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Planilla Data Added')

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AsignarCreateView, self).form_valid(form)

#----------Lista mensajeros Ruta a imprimir -------------
class AsignarListview(CustodiaPermisoMixin, ListView):
    context_object_name = "planillas" 
    template_name = "ruta/asignado_planillas.html"
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = courrier.objects.buscar_producto(kword, order)
        return queryset

class DestinoCreate(CreateView):
    template_name = "ruta/destino.html"
    form_class = DestinoForm
    success_url = '.'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Planilla Data Added', )

        return render(request, self.template_name, {'form': form})

class DescargueCreateView(CreateView, ListView):
   
    template_name = "ruta/descargue-destino.html"
    form_class = DescargueForm
    success_url = '.'

    
    def get_queryset(self):
        lista = Descargue.objects.filter(user=self.request.user).order_by('-fecha')[:5]
        return lista 

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(DescargueCreateView, self).form_valid(form)

class HistorialListview(ListView):
    context_object_name = "historial" 
    template_name = "ruta/historial.html"
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", "")
        queryset = Recepcion.objects.filter(guia__id_guia__icontains= kword,)
        return queryset

class InformeRutaCiudadListView(ListView):
    template_name = "ruta/informe_ruta_ciudad.html"
    context_object_name = 'lista'

    def get_queryset(self):
        destino = self.request.GET.get("destino", "")
        queryset = Guia.objects.filter(origen__contains= destino, estado_destino = True )
        return queryset
    
    def get_count(self):
        queryset = Guia.objects.filter(estado_destino = True)
        return queryset

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto ['lista'] = self.get_queryset()[:8]
        contexto ['count'] = self.get_queryset().count
        return contexto  

        
#---------------appi----------------------------
# from .serializers import(
#     CargueSerializer,
#     FisicoSerializer
# )


# from rest_framework.generics import (
#     ListAPIView,
#     CreateAPIView,
# )

# class FisicoListApiView(LoginRequiredMixin, ListAPIView):
#     serializer_class = FisicoSerializer

#     def get_queryset(self):
#         kword = self.request.query_params.get('kword', '')

#         return courrier.objects.filter(
#             courrier__icontains =kword
#         )

# class RegistrarCargue(CreateAPIView):
#     queryset = Cargue.objects.all()
#     serializer_class = CargueSerializer
#     permission_classes = [permissions.AllowAny]

#------------------Cargue----------------------------
# class CargueCreateView( CreateView):
#     template_name = "ruta_bootstrap/add_programador.html"
#     form_class = CargueForm
#     success_url = '.'
#     context_object_name = 'coin_lst'

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return super(CargueCreateView, self).form_valid(form)


#-------------lista filtro planilla----------------------
# class PLanillaListView(ListView): 
#     template_name ='ruta/lista_planillas.html'
#     context_object_name = 'lista'
    
#     def get_queryset(self):

#         nombre = self.kwargs['id']
#         lista = Planilla.objects.filter(
#         cargue__id = nombre
#     )   
#         return  lista

#--------------busqueda por palabra clave------------
# class ListPlanillasBykword(ListView):
#     template_name = "ruta_bootstrap/add_programador.html"
#     context_object_name = 'planillask'
#     model = Cargue
#     fields = ['__all__']
#     ordering = '-id'
#     paginate_by = '2'

    # def get_queryset(self):
    #     print('*************')
    #     palabra_clave = self.request.GET.get("kword",)
    #     lista = Cargue.objects.filter(
    #         id = palabra_clave        
    # )      
    #     return lista
    
    #--------------Vista asignar a mensajero-----------------