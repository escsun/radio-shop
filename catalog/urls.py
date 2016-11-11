from django.conf.urls import url
from .views import catalog_index, catalog_product_detail


urlpatterns = [
    url(r'^$', catalog_index, name='index'),
    url(r'^category/(?P<id>\d+)/$', catalog_index, name='category'),
    url(r'^category/(?P<id>\d+)/(?P<per_page>\d{2,3})/$', catalog_index, name='category'),
    url(r'^product/(?P<id>\d+)/$', catalog_product_detail, name='product'),
]