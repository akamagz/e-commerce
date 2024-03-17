from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Products, Order

def index(request):
    product_objects = Products.objects.all()

    # SEARCH 
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(name__icontains=item_name)
    
    # PAGINATION
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})

def detail(request,id):
    product_object = Products.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product_object':product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        fullname = request.POST.get('fullname', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        province = request.POST.get('province', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")
    
        order = Order(items=items,fullname=fullname,email=email,address=address,city=city,province=province,zipcode=zipcode,total=total)
        order.save()
        messages.success(request,f'Order was placed successfully.')

    return render(request, 'shop/checkout.html')

