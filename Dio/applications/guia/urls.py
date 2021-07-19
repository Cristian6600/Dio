from django.urls import path
from . import views

urlpatterns = [
path('lista-cliente/', views.ProductListView.as_view()),

]