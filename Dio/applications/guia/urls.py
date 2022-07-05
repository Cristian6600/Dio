from django.urls import path
from . import views
# from applications.guia.views import 
from . views import export

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
        views.FisicoCreateView.as_view(), 
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

    path(
        'upload/', 
        views.ima_cargar.as_view(), 
        name='index'
    ),

    
    

    # path(
    #     'prueba/',
    #     views.pruebaView.as_view(),
    #     name = 'prueba',
    # ),

    # path(
    #     'lista-guia-update/', 
    #     views.GuiaListView.as_view(), 
    #     name='lista-guia-update',
    # ),
    # path(
    #     'guia-update/<pk>/',
    #      views.GuiaUpdateView.as_view(),
    #      name='guia-bolsa-update',
    # ),
    
    ]