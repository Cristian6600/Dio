from django.shortcuts import render
from django.views.generic import ListView
from.models import datos_g, Orden
from .utils import render_to_pdf
from django.http import HttpResponse
from django.core.paginator import Paginator
from applications.users.mixins import CustodiaPermisoMixin
from django.db.models import Q
from django import template
from django.views.generic.dates import TodayArchiveView

register = template.Library()

class OrdenListView(CustodiaPermisoMixin, ListView):
    template_name = "datos_g/orden_guia.html"
    paginate_by = 8

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Orden.objects.order_by('-fecha'
        ). exclude(orden = -1). exclude(orden =-2).exclude(orden =-3).exclude(orden =-4
        ).exclude(orden =-5).exclude(orden =-6).exclude(orden =-7).exclude(orden =-8
        ).exclude(orden =-9).exclude(orden =-9).exclude(orden =-10).exclude(orden =-11).filter(orden__icontains=kword)
        return queryset
        

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
from django.db.models import Count
class OrdenAgendaListView(CustodiaPermisoMixin, ListView):
    template_name = "datos_g/orden_guia_agendamiento.html"
    # queryset = Orden.objects.order_by("orden")
    context_object_name = 'orden'
    paginate_by = 20

    def get_queryset(self):
        queryset = Orden.objects.filter(tipo = 1).order_by('-orden')
        return queryset

    def get_queryset_cont(self):
        queryset = Orden.objects.annotate(
            contar = Count('orden_dat_g', filter=Q(orden_dat_g__mot = 20)))
        return queryset

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto ['orden'] = self.get_queryset()
        contexto ['contar'] = self.get_queryset_cont().count
        return contexto  

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

