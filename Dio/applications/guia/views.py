from django.db.models import fields
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
import csv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import guiafisicoForm, ImgForm
from . models import Guia, img
from applications.users.mixins import CustodiaPermisoMixin, MesaPermisoMixin
from django.shortcuts import render
from .utils import render_to_pdf

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
    
class FisicoCreateView(CustodiaPermisoMixin, LoginRequiredMixin, CreateView, ListView):
    template_name = "guia/guia-fisico.html"
    # model = Guia
    # fields = ['id_guia', 'seudo', 'bolsa', 'user']
    form_class = guiafisicoForm
    paginate_by = '5'
    success_url = '.'   
    
    def get_queryset(self):
        return Guia.objects.filter(user=self.request.user).order_by('-fecha')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(FisicoCreateView, self).form_valid(form)

class ImgCreateView(CreateView):
    template_name = "guia/img_prueba.html"  
    form_class = ImgForm
    success_url = '.'

@login_required
def handleMultipleImagesUpload(request):
        if request.method == "POST":
            images = request.FILES.getlist('images')

            for image in images:
                img.objects.create(image = image)

            uploaded_images = img.objects.all()
            return JsonResponse({"imagenes": [{"url": image.image.url} for image in uploaded_images]})
        return render(request, "index.html")    

#--------Impresion por guia--------------
class GuiaListView(CustodiaPermisoMixin, ListView):
    template_name = "guia/imprimir_guia.html"
    context_object_name = 'guia'

    def get_queryset(self, ):
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

@login_required
def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        'CODIGO DE OFICINA', 'NOMBRE OFICINA', #1
        'DIRECCION DESTINO', 'CIUDAD DESTINO', #2
        'TELEFONO', 'CEDULA',          #3
        'OBSERVACION', 'PSEUDOCODIGO', #4 
        'BOLSA', 'TIPO DE EMISION',    #5
        'PROCESO',
        ])

    for guia in Guia.objects.filter(
        id_est = 2, mot = 3, producto = 3
        ).values_list(
        'id_ciu__id', 'guia_d_g__oficina', 
        'direccion', 'id_ciu__ciudad',
        'tel', 'd_i', 
        'destinatario', 
        'seudo', 'bolsa', 
        'seudo__t_emi'):
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
        'PSEUDOCODIGO', 'OBSERVACION', #4 
        'TIPO ENTREGA', 'BOLSA', #5
        'TIPO DE EMISION', 'PROCESO', #6 
        ])

    for guia in Guia.objects.filter(id_est = 2, mot = 3).values_list(
        'id_ciu__id', 'id_ciu__ciudad', #1
        'direccion', 'tel', #2
        'd_i', 'destinatario', #3
        'seudo', 'seudo', #4
        'proceso__cod_dir', 'bolsa', #5
        'seudo__t_emi',
        ).exclude(producto = 3):
        
        writer.writerow(guia)

    return response
     



    

