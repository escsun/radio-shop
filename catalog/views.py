from django.shortcuts import render
from .models import Category, Product, Value
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist


def catalog_index(request, id=None, per_page=20):
    categories = Category.objects.filter(parent_id=id)

    try:
        category = Category.objects.get(id=id)
    except ObjectDoesNotExist:
        category = Category.objects.none()

    if not categories:
        products_list = Product.objects.filter(category_id=id, is_available=True)
        paginator = Paginator(products_list, per_page=per_page)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        if not products:
            messages.error(request, "В данной категории товаров нет")
        return render(request, 'catalog_products.html', {
            "products": products,
            "category": category,
            'products_list': products_list
        })
    return render(request, 'catalog_base.html', {
        "categories": categories,
        'category': category
    })


def catalog_product_detail(request, id):
    product = Product.objects.get(id=id)
    values = Value.objects.filter(product_id=id)
    return render(request, 'catalog_product_detail.html', {
        "product": product,
        'values': values
    })