from django.urls import path
from . import views

app_name = "gatos_g"

urlpatterns = [
    path(
        'orden-impresion/',
         views.OrdenListView.as_view(),
         name='datos-cliente',
    ),

    path(
        'listar-guias/<id_datos_g>/',
        views.ListGuiaPdf.as_view(),
        name = 'impresion-guia',
    ),
]