from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Value
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from cart.forms import CartAddProductForm


def catalog_index(request, id=None):
    categories = Category.objects.filter(parent_id=id)

    try:
        category = Category.objects.get(id=id)
    except ObjectDoesNotExist:
        category = Category.objects.none()

    if not categories:
        products_list = Product.objects.filter(category_id=id, is_available=True)
        paginator = Paginator(products_list, per_page=25)
        page = request.GET.get('page')
        cart_product_form = CartAddProductForm()
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
            "cart_product_form": cart_product_form
        })
    response = render(request, 'catalog_base.html', {
        "categories": categories,
        "category": category
    })
    return response


def catalog_product_detail(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.get(id=product.category.id)
    values = Value.objects.filter(product_id=id)
    return render(request, 'catalog_product_detail.html', {
        "product": product,
        "values": values,
        "category": category
    })