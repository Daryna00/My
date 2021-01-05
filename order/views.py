from django.shortcuts import render, redirect
from .models import Order
from .form import OrderForm
from django.http import Http404

def index(request):
    return render(request, 'order/create.html')

def create_order(request):
    data = {}
    if request.method == "GET":
        order_form = OrderForm()
        data['order_form'] = order_form
        return render(request, 'order/create.html', context=data)
    elif request.method == "POST":
        order_form = OrderForm(request.POST, request.FILES)
        order_form.save()
        return redirect('/product/list')


def delete_order(request, slug):
    data = {}
    if not request.user.is_authenticated or not Order.objects.filter(slug=slug).exists():
        raise Http404
    order = Order.objects.get(slug=slug)
    if request.method == "GET":
        data['order'] = order
        return render(request, 'order/delete_order.html', context=data)
    elif request.method == "POST":
        order.delete()
        return redirect('/product/list')

def order_detail(request, id: int):
    data = {}

    order = Order.objects.get(id=id)
    data['order'] = order
    return render(request, 'order/details_order.html', data)


def order_list(request):
    data = {}
    all_order = Order.objects.all()
    data['order'] = all_order
    return render(request, 'order/list_order.html', context=data)
