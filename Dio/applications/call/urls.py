from django.urls import path
from . import views

app_name = "call_app"

urlpatterns = [
    path(
        'call-consultar/',
         views.CallListView.as_view(),
         name='lista-call',
    ),
    path(
        'call-update/<int:pk>/',
         views.CallUpdateView.as_view(),
         name='lista-call-update',
    ),
    
    path(
        'call-auditoria/',
         views.AuditoriaListView.as_view(),
         name='lista-call-auditoria',
    ),
    
    path(
        'call-create-auditoria/',
         views.AuditoriaCreateView.as_view(),
         name='create-call-auditoria',
    ),
    

     ]