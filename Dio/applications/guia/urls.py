from django.urls import path
from . import views

app_name = "producto_app"

urlpatterns = [
    path(
        'lista-cliente/',
         views.ProductListView.as_view(),
         name='lista-cliente',
    ),

    path(
        'producto/detalle/<pk>/', 
        views.ProductDetailView.as_view(),
        name='producto-detail',
    ),

    path(
        'add-fisico-g/',
        views.bolsaCreateView.as_view()),

    ]