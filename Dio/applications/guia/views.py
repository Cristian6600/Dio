from re import template
from django.db.models import fields
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from datetime import date
from django.utils.timezone import datetime #important if using timezones
import csv
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View
from django.views.generic.detail import SingleObjectMixin
from .forms import guiafisicoForm, ImgForm, UpdateCourrierForm
from . models import Guia, img
from applications.users.mixins import CustodiaPermisoMixin, MesaPermisoMixin
from django.shortcuts import render
from .utils import render_to_pdf
from django.db.models import Count
from django.template.defaulttags import register
from applications.fisico.models import Fisico
from applications.tracking.models import Rastreo

@register.filter
def cuts(value):
    return (value)[4:10]

@register.filter
def cadena_texto(value):
    return str(value)

class TrackingView(ListView):
    template_name = "producto/tracking.html"

    def get_queryset(self):
        

        queryset = Rastreo.objects.all()
        return queryset

class ProductListView(LoginRequiredMixin, ListView):
    template_name = "producto/cliente.html"
    paginate_by = 4

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Guia.objects.buscar_producto(kword, order)
        return queryset
           
class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "producto/detail.html"
    model = Guia

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        context['recepcion_list'] = Guia.objects.all()[:1]
        return context

from django.core.paginator import Paginator   
class FisicoCreateView(CustodiaPermisoMixin, LoginRequiredMixin, CreateView, ListView):
    template_name = "guia/guia-fisico.html"
    form_class = guiafisicoForm
    success_url = '.'   
    
    def get_queryset(self):
        vargui = Guia.objects.filter(user=self.request.user).order_by('-fecha')[:5]
        paginator = Paginator(vargui, 25)
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        return vargui
    
    def get_cantidad(self):
        # return Guia.objects.filter(user=self.request.user).filter('fecha__day')
        return Guia.objects.filter(user=self.request.user, fecha__contains=datetime.today().date())

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(FisicoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto ['page_obj'] = self.get_queryset()
        contexto ['form'] = self.form_class
        contexto ['count'] = self.get_cantidad().count
        return contexto

class ImgCreateView(CreateView):
    template_name = "guia/img_prueba.html"  
    form_class = ImgForm
    success_url = '.'


# @permission_required('fisico.add_mesa')
# def handleMultipleImagesUpload(request):
        
#         if request.method == "POST":
#             images = request.FILES.getlist('images')

#             for image in images:
#                 img.objects.create(image = image, user = request.user)

           
#             uploaded_images = img.objects.all()
#             count = uploaded_images
#             # return JsonResponse({"imagenes": [{"url": image.image.url} for image in uploaded_images]})
#             return HttpResponse("Total guias digitalizadas" + " " + str(len(images)))
#         return render(request, "index.html")  
from django.contrib import messages
class ima_cargar(MesaPermisoMixin, View):
    form_class = ImgForm
    template_name = "index.html"
    success_url = '.'
    initial = {'key': 'value'}
    model = img
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        kword = self.request.GET.get('kword')
        contact_list = img.objects.filter(
            user = request.user,
            id_guia = kword
        )
        paginator = Paginator(contact_list, 5) 

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count_day = img.objects.filter(
            user=self.request.user, 
            fecha__contains=datetime.today().date()).count
        data = {
            'page_obj': page_obj,
            'count': count_day
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
                images = request.FILES.getlist('images')
            
                for image in images:
                    img.objects.create(image = image, user = request.user)
    
                
                uploaded_images = img.objects.all()
                count = uploaded_images
            # return JsonResponse({"imagenes": [{"url": image.image.url} for image in uploaded_images]})
                # return HttpResponse("Total guias digitalizadas" + " " + str(len(images)))
                
                return render(request, 'guia/post_imagen.html', {'contar':str(len(images))})

        return render(request, self.template_name)

#--------Impresion por guia--------------
class GuiaListView(CustodiaPermisoMixin, ListView):
    template_name = "guia/imprimir_guia.html"
    context_object_name = 'guia'

    def get_queryset(self):
        queryset = Guia.objects.filter(
            id_guia=self.request.GET.get('id_guia'),
        )
        return queryset   
        
#-------------PDF impresion por guia--------------
class BuscarGuiaPdf(CustodiaPermisoMixin, ListView):
    # template_name = "guia/gui_pdf.html"
    # model = Guia
    # fields = ('__all__')
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['buscar']
        guia = Guia.objects.filter(id_guia = nombre)
        data = {
            'count': guia.count(),
            'guias': guia
        }
        pdf = render_to_pdf('guia/gui_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class MensajeroListView(CustodiaPermisoMixin, ListView ):
    template_name = "guia/mensajero_ruta.html"
    context_object_name = 'guia_mensajero'
    form_class = UpdateCourrierForm
    model = Fisico
    # success_url = reverse_lazy('producto_app:courrier-ruta')

    def get_queryset(self):
        queryset = Fisico.objects.all(
            # id_guia=self.request.GET.get('guia'),
        )
        return queryset   

    def get_object(self,queryset=None):  
        queryset = Fisico.objects.all()
        return super(MensajeroListView,self).get_object(queryset)

    

    def post(self, request, *args, **kwargs):
    
        # From BaseUpdateView
        self.object = self.get_object()

        # From ProcessFormView
        form = self.get_form()
        self.form = form
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)

# class MensajeroUpdateView(UpdateView):
#     template_name = "guia/mensajero_ruta.html"
#     model = Fisico
#     fields = ['mot',]
    # success_url = reverse_lazy('producto_app:courrier-ruta')

    def get_success_url(self):
        return reverse_lazy('producto_app:courrier-ruta')

@login_required
def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        'CODIGO DE OFICINA', 'NOMBRE OFICINA', #1
        'DIRECCION DESTINO', 'CIUDAD DESTINO', #2
        'TELEFONO', 'CEDULA',          #3
        'NOMBRE_USUARIO', 'PSEUDOCODIGO', #4 
        'BOLSA', 'TIPO DE EMISION',    #5
        'PROCESO',
        ])

    for guia in Guia.objects.filter(
        id_est = 2, mot = 3, producto = 3
        ).values_list(
        'guia_d_g__oficina', 'guia_d_g__oficina__nom_ofi', 
        'direccion', 'id_ciu__ciudad',
        'tel', 'd_i', 
        'destinatario', 
        'seudo', 'bolsa', 
        'proceso__tipo_e', 'seudo__producto__homologacion'):
        writer.writerow(guia)
        
    return response

@login_required
def export_address(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        'COD DANE', 'CIUDAD', #1
        'DIRECCION 1', 'TELEFONO', #2
        'CEDULA', 'NOMBRE_USUARIO', #3
        'PSEUDOCODIGO', #4 
        'TIPO ENTREGA', 'BOLSA', #5
        'TIPO DE EMISION', 'PROCESO', #6 
        ])

    for guia in Guia.objects.filter(id_est = 2, mot = 3).values_list(
        'id_ciu__id', 'id_ciu__ciudad', #1
        'direccion', 'tel', #2
        'd_i', 'destinatario', #3
        'seudo', #4
        'proceso__cod_dir', 'bolsa', #5
        'proceso__tipo_e', 'seudo__producto__homologacion'
        ).exclude(producto = 3):
        
        writer.writerow(guia)
        
    return response


# class GuiaListView(ListView):
#     template_name = "guia/update_list_guia.html"
#     model = Guia
#     paginate_by = 5

#     def get_queryset(self):
#         print('*******')
#         palabra_clave = self.request.GET.get("kword")
#         lista = Guia.objects.filter(
#             id_guia = palabra_clave
#         )
#         return lista
        # return Guia.objects.order_by('-fecha_bolsa')


# class GuiaUpdateView(UpdateView):
#     template_name = "guia/bolsa_update.html"
#     model = Guia
#     fields = ['bolsa',]
#     success_url = reverse_lazy('producto_app:lista-guia-update')
    

    
     



    

