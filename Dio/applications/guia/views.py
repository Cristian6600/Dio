
from django.db.models import fields
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import guiafisicoForm, ImgForm
from . models import Guia, img


class ProductListView(LoginRequiredMixin, ListView):
    template_name = "producto/cliente.html"
    model = Guia
    paginate_by = 5
    success_url = '.'
    # page_kwarg = 'page'
           
class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "producto/detail.html"
    model = Guia

class bolsaCreateView(LoginRequiredMixin, CreateView, ListView):
    template_name = "guia/guia-fisico.html"
    model = Guia
    fields = ['id_guia', 'seudo', 'bolsa', 'user']
    # form_class = guiafisicoForm
    success_url = '.'
    paginate_by = '5'
    context_object_name = 'stu'
    
    def get_queryset(self):
        return Guia.objects.order_by('-fecha')
    
    def get_queryset(self):
        return Guia.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(bolsaCreateView, self).form_valid(form)

class ImgCreateView(CreateView):
    template_name = "guia/img_prueba.html"  
    form_class = ImgForm
    success_url = '.'

# @login_required
def handleMultipleImagesUpload(request):
        if request.method == "POST":
            images = request.FILES.getlist('images')

            for image in images:
                img.objects.create(image = image)

            uploaded_images = img.objects.all()
            return JsonResponse({"imagenes": [{"url": image.image.url} for image in uploaded_images]})
        return render(request, "index.html")    



    

