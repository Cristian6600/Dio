#
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'panel/', 
        views.PanelHomeView.as_view(),
        name='index',
    ),
    path(
        'panel/', 
        views.HomePage.as_view(),
        name='panel',
    ),
    path(
        'mixin/', 
        views.TemplatePruebaMixin.as_view(),
        name='mixn',
    ),
    path(
        'publico/', 
        views.probando.as_view(),
        name='publico',
    ),
    
    path(
        'contacto/', 
        views.Contacto.as_view(),
        name='contacto',
    ),
]