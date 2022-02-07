from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from applications.guia.models import Guia
from django.urls import reverse_lazy
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
    






