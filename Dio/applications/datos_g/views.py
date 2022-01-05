from django.shortcuts import render
from django.views.generic import CreateView, ListView
from.models import datos_g, Orden
from .utils import render_to_pdf
from django.http import HttpResponse

class OrdenListView(ListView):
    template_name = "datos_g/orden_guia.html"
    model = Orden
    fields = ('__all__')
    context_object_name = 'orden'

class ListGuiaPdf(ListView):
        
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_datos_g']
        guia =datos_g.objects.filter(orimp = nombre)
        data = {
            'count': guia.count(),
            'empleados': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
