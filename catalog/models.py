from django.db import models
from django.utils.html import mark_safe
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Модель категорий - Список категорий товаров"""
    name = models.CharField(max_length=254, verbose_name="Имя", db_index=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name="Категория")
    image = models.ImageField(verbose_name="Изображение", default="category/no-image.png", upload_to="category")
    position = models.PositiveIntegerField(default=0, verbose_name="Позиция")

    class MPTTMeta:
        order_insertion_by = ["position"]

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категорию"

    def __str__(self):
        return self.name

    def image_thumbnail(self):
        if self.image:
            image_thumb = '<img src="/media/%s" width="100">' % self.image
            return mark_safe(image_thumb)
        else:
            return 'Изображения нет'
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Миниатюра"


class Product(models.Model):
    """Модель продуктов - Товары на сайте"""
    # Код товара равен CODE_OFFSET
    CODE_OFFSET = 1000

    name = models.CharField(max_length=254, verbose_name="Базовое имя")
    name_values = models.CharField(max_length=254, verbose_name="Имя")
    price = models.FloatField(verbose_name="Цена", blank=True, null=True)
    code = models.CharField(max_length=32, verbose_name="Код товара", blank=True, null=True,)
    is_available = models.BooleanField(default=True, verbose_name="В наличие")
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat', verbose_name="Категория")
    image = models.ImageField(verbose_name="Изображение", default="product/no-image.png", upload_to="product")
    position = models.PositiveIntegerField(verbose_name="Позиция", default=10)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Name(models.Model):
    """Модель наименований"""
    name = models.CharField(max_length=32, verbose_name="Наименование", unique=True)

    class Meta:
        verbose_name_plural = "Наименования"
        verbose_name = "Наименование"

    def __str__(self):
        return self.name


class Value(models.Model):
    """Модель значений для наименований"""
    name = models.ForeignKey(Name, verbose_name="Наименование")
    product = models.ForeignKey(Product, null=True, verbose_name="Товар")
    value = models.CharField(max_length=64, null=True, verbose_name="Значение")
    visible = models.BooleanField(default=1, verbose_name="Отображать")

    class Meta:
        verbose_name_plural = "Характеристики"
        verbose_name = "Характерстика"

    def __str__(self):
        return "%s - %s" % (self.name, self.value)
