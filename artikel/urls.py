from django.urls import path
from . import views

app_name = 'artikel'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:type_slug>/', views.product_list, name='product_list_by_type'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
]
