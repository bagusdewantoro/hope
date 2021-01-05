from django.urls import path
from . import views

app_name = 'artikel'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('awareness/', views.awareness_list, name='awareness_list'),
    path('awareness/<int:year>/<int:month>/<int:day>/<slug:awareness>/', views.awareness_detail, name='awareness_detail'),
    path('<slug:type_slug>/', views.product_list, name='product_list_by_type'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
