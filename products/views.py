

from django.http import HttpResponse
from django.shortcuts import render

from products.forms import ContactModelForm
from products.models import Category, Product

def filter_category(request, cat_pk=None):
    model_form = ContactModelForm()
    cats = Category.objects.all()
    prods = Product.objects.all()
    if cat_pk:
        prods = Product.objects.filter(category=cat_pk)
    else:
        prods = Product.objects.all()
    if request.method == 'POST':
        model_form = ContactModelForm(request.POST)
        if model_form.is_valid():
            print(model_form.is_valid)
            model_form.save()
        else:
            print(model_form.errors)
            context = {'error': model_form.errors, 'model_form': model_form, 'products': prods, 'categories': cats, }

    context = {'products': prods, 'categories': cats, 'model_form': model_form}
    return render(request, 'products/home.html', context)


def get_product(request, pk=None):
    model_form = ContactModelForm()
    cats = Category.objects.all()
    prods = Product.objects.all()
    if Product.objects.filter(pk=pk).exists():
        product = Product.objects.get(pk=pk)
        context = {'product': product, 'categories': cats, 'model_form': model_form}
        return render(request, 'products/detail.html', context)
    else:
        return render(request, 'utils/404.html')

def get_home(request, cat_pk=None):
    model_form = ContactModelForm()
    cats = Category.objects.all()
    prods = Product.objects.all()
    if request.method == 'POST':
        model_form = ContactModelForm(request.POST)
        if model_form.is_valid():
            print(model_form.is_valid)
            model_form.save()
        else:
            print(model_form.errors)
            context = {'error': model_form.errors, 'model_form': model_form, 'products': prods, 'categories': cats}

    context = {'products': prods, 'categories': cats, 'model_form': model_form}
    return render(request, 'products/home.html', context)


def get_product(request, pk=None):
    model_form = ContactModelForm()
    cats = Category.objects.all()
    prods = Product.objects.all()
    if Product.objects.filter(pk=pk).exists():
        product = Product.objects.get(pk=pk)
        context = {'product': product, 'categories': cats, 'model_form': model_form}
        return render(request, 'products/detail.html', context)
    else:
        return render(request, 'utils/404.html')