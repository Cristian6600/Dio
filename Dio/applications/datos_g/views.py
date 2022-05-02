from django.shortcuts import render
from django.views.generic import ListView
from.models import datos_g, Orden
from .utils import render_to_pdf
from django.http import HttpResponse
from applications.users.mixins import CustodiaPermisoMixin
from django.db.models import Q
from django import template
from django.views.generic.dates import TodayArchiveView

register = template.Library()

class OrdenListView(CustodiaPermisoMixin, ListView):
    template_name = "datos_g/orden_guia.html"
    queryset = Orden.objects.order_by('-fecha'). exclude(orden = -1)
    context_object_name = 'orden'

class ListGuiaPdf(CustodiaPermisoMixin, ListView):
        
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_datos_g']
        guia =datos_g.objects.filter(orimp = nombre, seudo_dg__user=self.request.user). order_by('seudo_dg__id_guia' ).exclude(seudo_dg__mot = 3)
        data = {
            'count': guia.count(),
            'pdf_guia': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

##################### Agendamientos ###############################

class OrdenAgendaListView(CustodiaPermisoMixin, ListView):
    template_name = "datos_g/orden_guia_agendamiento.html"
    queryset = Orden.objects.filter(orden = -7).order_by('-fecha')
    context_object_name = 'orden'
    paginate_by = 1

class Lista_gendamientosListView(CustodiaPermisoMixin, TodayArchiveView, ListView):
    date_field = "pub_date"
    allow_future = True
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_agenda']
        guia =datos_g.objects.filter(
            orimp = nombre,
            id_ciu__departamento=self.request.user.ciudad.departamento
            )
        data = {
            'count': guia.count(),
            'guia_agenda': guia
        }
        pdf = render_to_pdf('datos_g/pdf-agenda.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

