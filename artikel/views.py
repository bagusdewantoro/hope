from django.shortcuts import render, get_object_or_404
from artikel.models import Product, Size, Type, StockLog, Awareness

# PRODUCT ===============================================
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


# AWARENESS ===============================================
def awareness_list(request):
    awarenesses = Awareness.published.all()
    return render(request,
                    'artikel/awareness/list.html',
                    {'awarnesses': awarnesses})

def awareness_detail(request, year, month, day, awareness):
    awareness = get_object_or_404(Awareness, slug=awareness,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    return render(request,
                    'artikel/awareness/detail.html',
                    {'awareness': awareness})
