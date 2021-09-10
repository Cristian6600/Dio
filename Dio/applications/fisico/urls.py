from django.urls import path
from . import views

app_name = "fisico_app"

urlpatterns = [
    
    path('add-fisico-paquete/', views.bolsaCreateView.as_view()),
    path('lista-fisico/', views.FisicoListView.as_view()),

]