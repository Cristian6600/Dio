from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.template import loader
import csv
from . models import Bd_clie
from applications.fisico.models import Paquete
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from applications.users.mixins import SigPermisoMixin
from django.views import View, generic
from .forms import No_fisicoForm
from . models import No_fisico

@login_required
def exportSig(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        'FECHA INGRESO', 'PSEUDOCÓDIGO', #1
        'NO IDENTIFICACIÓN', 'NOMBRE ', #2
        'PROCESO', 'ESTADO DE DAVIVIENDA',  #3
        'ESTADO DEL DISTRIBUIDOR', 'DESCRIPCIÓN O MOTIVO', #4
        'COD DIRECCIÓN', 'TIPO DE ENTREGA',#5
        'NOMBRE DEL PRODUCTO', 'CIUDAD', #6
        'COD OFICINA DEVOLUCIÓN', 'NOMBRE OFICINA DEVOLUCIÓN', #7
        'FECHA GESTIÓN', 'NO DIAS VISITAS', #8
        'TIPO DE ENTREGA INICIAL', 'BOLSA SEGURIDAD DE SALIDA', #9
        'CODIGO DIRECCION', 'DIRECCION CITA',#10
        'COD', 'NOMBRE OFICINA', #11
        'MUNICIPIO','DIRECCION', #12
        'TIPO DE EMISION','ID REGISTRO ',#13
        'ORIGEN', 'DESTINO',  #14
        'FECHA-DESTINO' #15
          ])

    for guia in Bd_clie.objects.all().values_list(
        'guias__fecha', 'seudo_bd',   #1      
        'guias__d_i', 'guias__destinatario',#2
        'guias__guia_d_g__id_pro__producto', 'guias__cod_ins__descripcion', #3
        'guias__cod_ins__estado', 'guias__cod_ins__mot_est', #4
        'guias__proceso__cod_dir', 'guias__cod_ins__t_entrega', #5 
        'nom_pro__nom_producto', 'guias__id_ciu', #6
        'guias__id_ciu', 'guias__fecha_recepcion', #7
        'guias__fecha_recepcion', 'guias__cantidad', #8
        'guias__proceso__tipo_e', 'guias__bolsa', #9
        'guias__proceso__cod_dir', 'guias__direccion', #10
        'guias__guia_d_g__oficina', 'guias__guia_d_g__oficina__nom_ofi', # 11
        'guias__id_ciu__ciudad', 'guias__direccion', #12
        't_emi', 'guias__id_guia',#13
        'guias__origen', 'guias__destino', #14
        'guias__fecha_descargue', 
        
        ):
        
        
        writer.writerow(guia)
        response['Content-Disposition'] = 'attachment; filename="informe.csv"'

    return response

@login_required
def exportSig_paquete(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        
        'BOLSA', 'SEUDO', 'NOMBRE', 'CEDULA', 'NOMBRE PRODUCTO' ])

    for guia in Paquete.objects.all().values_list(
        'bolsa', 'seudo_id', 'seudo_id__nombre', 'seudo_id__cc', 'seudo_id__nom_pro'   #1      
       
        ):
        writer.writerow(guia)
        response['Content-Disposition'] = 'attachment; filename="paquete.csv"'
    return response

class Bd_clieListView(SigPermisoMixin, ListView):
    template_name = "bd/bd.html"
    context_object_name = 'bd'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Bd_clie.objects.buscar_bd(kword, order)
        return queryset

class No_fisicoCreateView(CreateView, ListView):
    template_name = "bd/faltante.html"
    form_class = No_fisicoForm
    success_url = '.'
    paginate_by = 16

    def get_queryset(self):
        return No_fisico.objects.all()




