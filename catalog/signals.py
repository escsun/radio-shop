from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Value


@receiver(post_save, sender=Value)
def add_name_and_code(sender, instance, **kwargs):
    """Устанавливает код товара и имя со значениями (name_values) на основе базового имени (name) """
    product = instance.product
    values = Value.objects.filter(product_id=product.id, visible=True)
    values_list = []
    for value in values:
        values_list.append(value.value)
    value_str = ' ' + ', '.join(values_list)
    product.name_values = product.name + value_str
    product.code = Product.CODE_OFFSET + Product.objects.get(pk=product.id).id
    product.save()