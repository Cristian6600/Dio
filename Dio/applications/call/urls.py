from django.urls import path
from . import views
from applications.call.views import  SolicitudUpdate
from django.contrib.auth.views import login_required
from django.conf.urls import url
	


app_name = "call_app"

urlpatterns = [
    path(
        'cac-consultar/',
         views.CacListView.as_view(),
         name='lista-call',
    ),
    path(
        'cac-update/<int:pk>/',
         views.CacUpdateView.as_view(),
         name='lista-call-update',
    ),
    
    path(
        'call-update-estado-call/<int:pk>/',
         views.CallEstadoUpdateView.as_view(),
         name='call-update-estado-call',
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

    #######CAC
    path(
        'call-consultar/',
         views.CallListView.as_view(),
         name='call-consultar',
    ),
    path(
        'call-update/<int:pk>/',
         views.CallUpdateView.as_view(),
         name='call-update',
    ),
    # url(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    # 
    path(
        'solicitud/editar/<int:pk>/',
         views.SolicitudUpdate.as_view(),
         name='call-updatesss',
    ),
    ]

     