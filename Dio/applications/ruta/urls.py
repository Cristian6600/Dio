from django.urls import path

from . import views

app_name = "producto_apps"

urlpatterns = [
    path(
        'add-cargue-ruta/',
        views.CargueCreateView.as_view()),

    path(
        'add-cargue-recepcion/',
        views.RecepcionCreateView.as_view()),
    
    ]