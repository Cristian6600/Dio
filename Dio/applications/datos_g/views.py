from django.shortcuts import render
from django.views.generic import ListView
from.models import datos_g, Orden
from .utils import render_to_pdf
from django.http import HttpResponse
from applications.users.mixins import CustodiaPermisoMixin
from django.db.models import Q

class OrdenListView(CustodiaPermisoMixin, ListView):
    template_name = "datos_g/orden_guia.html"
    queryset = Orden.objects.order_by('-fecha')
    context_object_name = 'orden'

# class OrdenAgendaListView(CustodiaPermisoMixin, ListView):
#     template_name = "datos_g/orden_guia_agendamiento.html"
#     queryset = Orden.objects.order_by('-fecha')
#     context_object_name = 'orden'
#     paginate_by = 1

class ListGuiaPdf(CustodiaPermisoMixin, ListView):
        
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_datos_g']
        guia =datos_g.objects.filter(orimp = nombre, seudo_dg__user=self.request.user). order_by('seudo_dg__id_guia' )
        data = {
            'count': guia.count(),
            'empleados': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

# class Lista_gendamientos(CustodiaPermisoMixin, ListView):
        
#     def get(self, request, *args, **kwargs):
#         nombre = self.kwargs['id_datos_g_agendamiento']
#         guia =datos_g.objects.all().filter(Q(seudo_dg__mot = 19) | Q(seudo_dg__mot= 20) | Q(seudo_dg__user=self.request.user))
#         data = {
#             'count': guia.count(),
#             'empleados': guia
#         }
#         pdf = render_to_pdf('datos_g/pdf-agenda.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')
