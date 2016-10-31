from django.conf.urls import url
from .views import categories_and_products, get_one_product


urlpatterns = [
    url(r'^category/(?P<id>\d+)/$', categories_and_products, name='category'),
    url(r'^product/(?P<id>\d+)/$', get_one_product, name='product'),
]