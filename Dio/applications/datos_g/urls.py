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
    
    ########impresion agendamientos########
    path(
        'orden-impresion-guia-agendamientos/',
         views.OrdenAgendaListView.as_view(),
         name='guia-buscar-agendamientos',
    ),
    
    path(
        'pdg-guia-agendamiento/<id_agenda>/',
         views.Lista_gendamientosListView.as_view(),
         name='pdg-guia-agendamiento',
    ),
    
    
    
]


# from django.urls import path
# from . import views

# app_name = "gatos_g"

# urlpatterns = [
#     path(
#         'orden-impresion/',
#          views.OrdenListView.as_view(),
#          name='datos-cliente',
#     ),

#     path(
#         'listar-guias/<id_datos_g>/',
#         views.ListGuiaPdf.as_view(),
#         name = 'impresion-guia',
#     ),
#     path(
#         'orden-impresion-guia/',
#          views.OrdenListView.as_view(),
#          name='guia-buscar',
#     ),
#     path(
#         'orden-impresion-guia-agendamiento/',
#          views.OrdenListView.as_view(),
#          name='guia-buscar-agendamiento',
#     ),
#     #Lista_gendamientos
#     path(
#         'listar-guias-a/<id_datos_g_agendamiento>/',
#          views.Lista_gendamientos.as_view(),
#          name='guia-buscar-agendamientos',
#     ),
    
# ]