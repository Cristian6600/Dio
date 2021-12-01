from django.urls import path

from . import views

app_name = "ruta_apps"

urlpatterns = [
    path(
        'add-cargue-ruta/',
        views.CargueCreateView.as_view(),
        name ='cargue-ruta'),

    path(
        'add-cargue-recepcion/',
        views.RecepcionCreateView.as_view(),
        name = 'cargue-recepcion'),

    path(
        'listar-planillas/',
        views.ListEmpleadosPdf.as_view(),
        
    ),
    path(
        'api/lenguaje/search/', 
        views.LenguajeListApiView.as_view(),
        name='lenguaje-buscar',
    ),

    path(
        'api/programador/register/', 
        views.RegistrarProgramador.as_view(),
        name='programador-register',
    ),

    path(
        'api/programador/register/', 
        views.RegistrarProgramador.as_view(),
        name='programador-register',
    ),
    
    ]