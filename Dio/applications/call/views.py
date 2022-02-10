from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, CreateView
from applications.guia.models import Guia
from applications.call.models import Auditoria
from django.urls import reverse_lazy
from .forms import CallfisicoForm
from django.db.models import Q
from applications.users.mixins import CallPermisoMixin

class CallUpdateView(CallPermisoMixin, UpdateView):
    template_name = "call/_update_form.html"
    model = Guia
    fields = ['direccion', 'id_ciu', 'postal', 'mot', 'cod_vis']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('call_app:lista-call')

class CallListView(CallPermisoMixin, ListView):
    template_name = "call/gestion.html"
    context_object_name = 'call'
    queryset = Guia.objects.filter(Q(id_est = 3), Q(mot=5) | Q(mot=6)| Q(mot=7)| Q(mot=8)). order_by('-fecha')
    context_object_name = 'call'
    paginate_by = 5
    
class AuditoriaListView(ListView):
    template_name = "call/auditoria.html"
    context_object_name = 'auditoria'
    queryset = Guia.objects.filter(mot = 21, estado=1)
    paginate_by = 5

class AuditoriaCreateView(CreateView):
    template_name = "call/create_auditoria.html"
    form_class = CallfisicoForm
    success_url = reverse_lazy('call_app:lista-call-auditoria')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AuditoriaCreateView, self).form_valid(form)
     
    




