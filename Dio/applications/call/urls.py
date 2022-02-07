from django.urls import path
from . import views

app_name = "call_app"

urlpatterns = [
    path(
        'call/',
         views.CallListView.as_view(),
         name='lista-call',
    ),
    path(
        'call-update/<pk>/',
         views.CallUpdateView.as_view(),
         name='lista-call-update',
    ),

     ]