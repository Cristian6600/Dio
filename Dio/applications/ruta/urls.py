from django.urls import path
from . import views


app_name = "ruta_apps"

urlpatterns = [
    path(
        'add-cargue-ruta/',
        views.CargueCreateView.as_view(),
        name ='cargue-ruta'
    ),

    path(
        'add-cargue-recepcion/',
        views.RecepcionCreateView.as_view(),
        name = 'cargue-recepcion'
    ),

    path(
        'listar-planillas/<full_name>/',
        views.ListEmpleadosPdf.as_view(),
        name = 'impresion',
    ),
    # urls de los servicios
    path(
        'api/lenguaje/search/', 
        views.FisicoListApiView.as_view(),
        name='lenguaje-buscar',
    ),
    path(
        'api/programador/register/', 
        views.RegistrarCargue.as_view(),
        name='programador-register',
    ),
    path(
        'lista/planillas/<full_name>', 
        views.PLanillaListView.as_view(),
        name='listar-planillas',
    ),

    path(
        'lista/planillas/buscar/', 
        views.ListPlanillasBykword.as_view(),
        name='listarr-planillas',
    ),
    
    ]