from django.urls import path
from . import views

app_name = "ruta_apps"

urlpatterns = [

    path(
        'add-cargue-recepcion/',
        views.RecepcioCreateView.as_view(),
        name = 'cargue-recepcion'
    ),

    path(
        'listar-planillas/<full_name>/',
        views.ListEmpleadosPdf.as_view(),
        name = 'impresion',
    ),
    

    path(
        'lista/planillas/asignar/', 
        views.AsignarCreateView.as_view(),
        name='asignar', 
    ),

     path(
        'lista/planillas/generar/', 
        views.AsignarListview.as_view(),
        name='planillas',
    ),

    path(
        'generar/destino/', 
        views.DestinoCreate.as_view(),
        name='destino'
    ),
    
    path(
        'generar/descargue/', 
        views.DescargueCreateView.as_view(),
        name='destino-descargue'
    ),
    
    path(
        'generar/historial/<int:guia__id_guia>/', 
        views.HistorialListview.as_view(),
        name='historial'
    ),
    
    
    
    ]