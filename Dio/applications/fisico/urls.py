from django.urls import path
from . import views

app_name = "fisico_app"

urlpatterns = [
    path(
        'add-fisico-paquete/',
         views.BolsaCreateView.as_view(),
         name = 'fisico-paquete',
         ),

    path('lista-fisico/', views.FisicoListView.as_view()),

    path(
        'estado-ruta/',
         views.EstadoRutaListView.as_view(),
         name = 'estado-ruta',
         ),


    

]