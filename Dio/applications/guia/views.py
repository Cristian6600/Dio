
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import guiafisicoForm
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

class bolsaCreateView(CreateView):
    template_name = "guia/guia-fisico.html"
    form_class = guiafisicoForm
    success_url = '.'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(bolsaCreateView, self).form_valid(form)

class imaCreateView(CreateView):
    template_name = "guia/add-img.html"
    

    def handleMultipleImagesUpload(request):
        if request.method == "POST":
            images = request.FILES.getlist('images')

            for image in images:
                img.objects.create(image = image)

            uploaded_images = img.objects.all()
            return JsonResponse({"images": [{"url": image.image.url} for image in uploaded_images]})
        return render(request, "index.html")    
    

    

    
