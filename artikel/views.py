from django.shortcuts import render, get_object_or_404
from artikel.models import Product, Size, Type, StockLog


def product_list(request, type_slug=None):
    type = None
    types = Type.objects.all()
    products = Product.objects.filter(available=True)
    if type_slug:
        type = get_object_or_404(Type, slug=type_slug)
        products = products.filter(type=type)
    return render(request,
                    'artikel/product/list.html',
                    {'type': type,
                    'types': types,
                    'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                    'artikel/product/detail.html',
                    {'product': product})
