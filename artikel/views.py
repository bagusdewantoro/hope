from django.shortcuts import render
from artikel.models import Product, Size, Type, StockLog
from django.views import generic

class ProductListView(generic.ListView):    # nama class boleh diganti, asal sama kaya di urls.py
    model = Product
    template_name = 'artikel/product_list.html'

class ProductDetailView(generic.DetailView):   # nama class boleh diganti, asal sama kaya di urls.py
    model = Product
