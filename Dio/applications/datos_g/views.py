from django.shortcuts import render
from django.views.generic import View, ListView
from.models import datos_g, Orden
from .utils import render_to_pdf
from django.http import HttpResponse

class OrdenListView(ListView):
    template_name = "datos_g/orden_guia.html"
    queryset = Orden.objects.order_by('-fecha')
    
    context_object_name = 'orden'

class ListGuiaPdf(ListView):
        
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_datos_g']
        guia =datos_g.objects.filter(orimp = nombre, seudo_dg__user=self.request.user)
        data = {
            'count': guia.count(),
            'empleados': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class MyView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Esto es una prueba!')