from django.urls import path
from . import views

app_name = "bd_app"

urlpatterns = [
    path(
        'bd-informe/',
         views.Bd_clieListView.as_view(),
         name='bd-Informe',
    ),

     ]