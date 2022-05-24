from dataclasses import field
from re import template
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, CreateView
from applications.guia.models import Guia, Guiap, TelefonoP
from applications.call.models import Auditoria
from django.urls import reverse_lazy
from .forms import CallfisicoForm, CallUpdateForm, CacUpdateForm, CallGuiaUpdateForm, SolicitudForm, PersonaForm
from django.db.models import Q
from applications.users.mixins import CallPermisoMixin
from . models import Telefono
from django.http import HttpResponse, HttpResponseRedirect


class CacUpdateView(CallPermisoMixin, UpdateView):
    template_name = "call/update_form.html"
    form_class = CacUpdateForm
    model= Guia
    # fields = ['direccion', 'id_ciu', 'postal', 'mot', 'cod_vis', 'motivo_call','oficina']
    success_url = reverse_lazy('call_app:lista-call')
    
    # def get_context_data(self, **kwargs):
    #     contexto = {}
    #     contexto ['lista'] = self.get_queryset()
    #     contexto ['form'] = self.form_class
    #     return contexto

class CallUpdateView(CallPermisoMixin, UpdateView):
    template_name = "call/call-update.html"
    form_class = CallUpdateForm
    second_form_class = CallGuiaUpdateForm
    model= Telefono
    second_model = Guia
    # fields = ['direccion', 'id_ciu', 'postal', 'mot', 'cod_vis', 'motivo_call','oficina']
    success_url = reverse_lazy('call_app:call-consultar')
    
    def get_context_data(self, **kwargs):
        context = super(CallUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        telefono = self.model.objects.get(id=pk)
        guia = self.second_model.objects.get(seudo_id=telefono.id)
        if 'form' not in context:
            context['form'] = self.form_class()
        
        if 'form2' not in context:
            context['form2'] =self.second_form_class(instance= guia)
        context['id']= pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        telefono = self.model.objects.get(id=id_solicitud)
        guia = self.second_model.objects.get(seudo_id=telefono.id)
        form = self.form_class(request.POST, instance=telefono)
        form2 = self.second_form_class(request.POST, instance=guia)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

            

    
class CallEstadoUpdateView(UpdateView):
    template_name = "call/update-estado-call.html"
    model = Telefono
    fields = ['motivo_call', 'observacion']
    success_url = reverse_lazy('call_app:call-consultar')

    
class CacListView(CallPermisoMixin, ListView):
    template_name = "call/cac_gestion.html"
    context_object_name = 'call'
    # queryset = Guia.objects.filter(Q(id_est = 3), Q(mot=5) | Q(mot=6)| Q(mot=7)| Q(mot=8)). order_by('-fecha')
    # context_object_name = 'call'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        
        producto = self.request.GET.get("producto", "")
        reason = self.request.GET.get("reason", "")
        seudo = self.request.GET.get("kword", "")
        fecha = self.request.GET.get("date_start", "")
        lista = Guia.objects.filter(id_est = 3, 
            producto__producto__contains = producto,
            mot__motivo__icontains = reason,
            fecha_recepcion__icontains = fecha
        ).filter(
            Q(seudo__seudo_bd__icontains=seudo)|
            Q(id_ciu__ciudad__icontains = seudo)|
            Q(d_i__icontains =seudo)|
            Q(id_guia__icontains = seudo)
        ).order_by("-motivo_call"
        ).exclude(mot = 1).exclude(mot = 22).exclude(mot = 21).exclude(mot = 20).exclude(mot=19)
        # .filter(
        #     Q(seudo__seudo_bd__icontains=seudo)|
        #     Q(id_ciu__ciudad__icontains = seudo)|
        #     Q(d_i__icontains =seudo)|
        #     Q(id_guia__icontains = seudo)
        #     ).filter(mot__motivo__icontains = reason).order_by("-motivo_call"
        #     ).exclude(mot = 1).exclude(mot = 22).exclude(mot = 21).exclude(mot = 20).exclude(mot=19)
        
        return lista

class CallListView(CallPermisoMixin, ListView):
    template_name = "call/call_gestion.html"
    context_object_name = 'call'
    # queryset = Guia.objects.filter(Q(id_est = 3), Q(mot=5) | Q(mot=6)| Q(mot=7)| Q(mot=8)). order_by('-fecha')
    # context_object_name = 'call'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        
        producto = self.request.GET.get("producto", "")
        reason = self.request.GET.get("reason", "")
        seudo = self.request.GET.get("kword", "")
        fecha = self.request.GET.get("date_start", "")
        lista = Guia.objects.filter(id_est = 3, 
            producto__producto__contains = producto,
            mot__motivo__icontains = reason,
            fecha_recepcion__icontains = fecha
        ).filter(
            Q(seudo__seudo_bd__icontains=seudo)|
            Q(id_ciu__ciudad__icontains = seudo)|
            Q(d_i__icontains =seudo)|
            Q(id_guia__icontains = seudo)
        #).order_by("-motivo_call"
        ).exclude(mot = 1).exclude(mot = 22).exclude(
            mot = 21).exclude(mot = 20).exclude(mot=19).exclude(
            telefono_guia__motivo_call= 11).exclude(
            telefono_guia__motivo_call= 12)
        # .filter(
        #     Q(seudo__seudo_bd__icontains=seudo)|
        #     Q(id_ciu__ciudad__icontains = seudo)|
        #     Q(d_i__icontains =seudo)|
        #     Q(id_guia__icontains = seudo)
        #     ).filter(mot__motivo__icontains = reason).order_by("-motivo_call"
        #     ).exclude(mot = 1).exclude(mot = 22).exclude(mot = 21).exclude(mot = 20).exclude(mot=19)
        
        return lista



class AuditoriaListView(ListView):
    template_name = "call/auditoria.html"
    context_object_name = 'auditoria'
    # queryset = Guia.objects.filter(mot = 21, estado=1)
    paginate_by = 5

    def get_queryset(self, **kwargs):
        
        ciudad = self.request.GET.get("ciudad", "")
        kword = self.request.GET.get("kword", "")
        fecha = self.request.GET.get("date_start", "")
        lista = Guia.objects.filter(mot = 21, estado=1).filter(
            fecha_recepcion__icontains = fecha,
            id_ciu__ciudad__icontains = ciudad
        ).filter(
            Q(mensajero__courrier__icontains =kword)|
            Q(seudo__seudo_bd__icontains=kword)
        )
            
        return lista

class AuditoriaCreateView(CreateView):
    template_name = "call/create_auditoria.html"
    form_class = CallfisicoForm
    success_url = reverse_lazy('call_app:lista-call-auditoria')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AuditoriaCreateView, self).form_valid(form)


     
#Vista eliminarfd-----------------------------------------
class SolicitudUpdate(UpdateView):
    model = TelefonoP
    second_model = Guiap
    template_name = 'call/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:solicitud_listar')


    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        telefono = self.model.objects.get(id=pk)
        guia = self.second_model.objects.get(seudof=telefono.id)
        if 'form' not in context:
           context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=guia)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        telefono = self.model.objects.get(id=id_solicitud)
        guia = self.second_model.objects.get(seudof=telefono.id)
        form = self.form_class(request.POST, instance=telefono)
        form2 = self.second_form_class(request.POST, instance=guia)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
        print("HOola")


