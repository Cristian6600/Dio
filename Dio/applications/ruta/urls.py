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
    
     
    # path(
    #     'guia/buscar/', 
    #     views.ConsultarImprimirGuiaListView.as_view(),
    #     name='Guia_imprimir',

    # ),
    
    

    #-----vista appi rest se desactiva por modificacion orden planillas

    # path(
    #     'api/lenguaje/search/', 
    #     views.FisicoListApiView.as_view(),
    #     name='lenguaje-buscar',
    # ),

    # path(
    #     'api/programador/register/', 
    #     views.RegistrarCargue.as_view(),
    #     name='programador-register',
    # ),

    # path(
    #     'lista/planillas/buscar/', 
    #     views.ListPlanillasBykword.as_view(),
    #     name='listarr-planillas',
    # ),

    #  path(
    #     'add-cargue-ruta/',
    #     views.CargueCreateView.as_view(),
    #     name ='cargue-ruta'
    # ),
    # path(
    #     'lista/planillas/<full_name>', 
    #     views.PLanillaListView.as_view(),
    #     name='listar-planillas',
    # ),
    
    ]