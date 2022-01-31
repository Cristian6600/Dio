from django.urls import path
from . import views

app_name = "producto_app"

urlpatterns = [
    path(
        'lista-cliente/',
         views.ProductListView.as_view(),
         name='lista-cliente',
    ),

    path(
        'producto/detalle/<pk>/', 
        views.ProductDetailView.as_view(),
        name='producto-detail',
    ),

    path(
        'add-fisico/', 
        views.bolsaCreateView.as_view(), 
        name='producto-crear',
    ),
    
    path(
        'guia-buscar/', 
        views.GuiaListView.as_view(), 
        name='guia-buscar',
    ),

    path(
        'buscar-guias/<buscar>/',
        views.BuscarGuiaPdf.as_view(),
        name = 'busca-guia',
    ),


    ]