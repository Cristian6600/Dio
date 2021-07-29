from django.urls import path
from . import views

app_name = "fisico_app"

urlpatterns = [
    path(
        'add-fisico/',
        views.InventarioCreateView.as_view(),
        name='fisico-ingreso',

    ),


    path('add-fisico-d/', views.bolsaCreateView.as_view()),

]