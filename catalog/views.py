from django.shortcuts import render
from .models import Category, Product, Value
from django.contrib import messages


def catalog_index(request, id=None):
    categories = Category.objects.filter(parent_id=id)
    if not categories:
        products = Product.objects.filter(category_id=id, is_available=True)
        category = Category.objects.get(id=id)
        if not products:
            messages.error(request, "В данной категории товаров нет")
        return render(request, 'catalog_products.html', {
            "products": products,
            'category': category
        })
    return render(request, 'catalog_base.html', {"categories": categories})


def catalog_product_detail(request, id):
    product = Product.objects.get(id=id)
    values = Value.objects.filter(product_id=id)
    return render(request, 'catalog_product_detail.html', {
        "product": product,
        'values': values
    })