
from django.db.models import fields
from django.shortcuts import render

from django.contrib import messages

from applications.fisico.models import Fisico

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

from django.views.generic import CreateView, View, ListView, UpdateView, DeleteView

from . models import Cargue, Planilla, Programador, Lenguaje, Recepcion

from .utils import render_to_pdf

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

from .forms import CargueForm
from .forms import RecepcionForm

#------------------Cargue----------------------------
class CargueCreateView(LoginRequiredMixin, CreateView):
    template_name = "ruta/add-ruta.html"
    model = Cargue
    form_class = CargueForm
    success_url = '.'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CargueCreateView, self).form_valid(form)


#----------------Recepcion------------------------

class RecepcionCreateView(CreateView, ListView ):
    # model= Recepcion
    # fields = ['planilla', 'motivo', 'estado', 'guia']
    template_name = "ruta/add-recepcion.html"
    form_class =  RecepcionForm
    initial = {'key':'value'}
    success_url = '.'
    context_object_name = 'stu'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recepcion Data Added')

        return render(request, self.template_name, {'form': form})

class RecepcionUpdateView(UpdateView):
    model = Recepcion
    fields = ['planilla', 'motivo', 'guia']
    template_name = 'updateForm.html'
    success_url = '.'

class RecepcionDeleteView(DeleteView):
    model = Recepcion
    template_name = "deleteForm.html"
    success_url = '.'

class ListEmpleadosPdf(ListView):

    def get_queryset(self):
        pass
        
    def get(self, request, *args, **kwargs):
        empleados = Planilla.objects.all()
        data = {
            'count': empleados.count(),
            'empleados': empleados
        }
        pdf = render_to_pdf('ruta/empleados.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

