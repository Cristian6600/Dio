from django.urls import path

from . import views
from .views import RecepcionCreateView, RecepcionUpdateView, RecepcionDeleteView

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

    path('student/edit/<int:pk>/',RecepcionUpdateView.as_view(),name="reUpdate"),
    path('student/edit/<int:pk>/',RecepcionDeleteView.as_view(),name="reDelete"),

    path(
        'listar-planillas/<id>/',
        views.ListEmpleadosPdf.as_view(),
        
    ),
    
    ]