from django.urls import path
from . import views

urlpatterns = [
path('add-fisico/', views.InventarioCreateView.as_view()),

]