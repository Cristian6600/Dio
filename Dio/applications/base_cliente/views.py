from django.shortcuts import render
import csv
from . models import Bd_clie
from django.http import HttpResponse
from django.views.generic import ListView

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
        'TIPO DE EMISION','ID REGISTRO ', ])#13

    for guia in Bd_clie.objects.all().values_list(
        'guias__fecha', 'seudo_bd',   #1      
        'guias__d_i', 'guias__destinatario',#2
        'guias__proceso', 'guias__id_est__Estado', #3
        'guias__id_est__Estado', 'guias__mot', #4
        'guias__proceso__cod_dir', 'guias__proceso__cod_dir', #5 #verificar
        'nom_pro', 'guias__id_ciu', #6
        'guias__id_ciu', 'guias__fecha_recepcion', #7
        'guias__fecha_recepcion', 'guias__cantidad', #8
        'guias__proceso__proceso', 'guias__bolsa', #9
        'guias__proceso__cod_dir', 'guias__direccion', #10
        'guias__guia_d_g__oficina', 'guias__guia_d_g__oficina', # 11
        'guias__id_ciu__ciudad', 'guias__direccion', #12
        't_emi', 'guias__id_guia',
        ):
        writer.writerow(guia)

    return response

class Bd_clieListView(ListView):
    template_name = "bd/bd.html"
    context_object_name = 'bd'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Bd_clie.objects.buscar_bd(kword, order)
        return queryset
