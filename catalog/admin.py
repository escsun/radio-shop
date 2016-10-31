from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Product, Name, Value
# Register your models here.


@admin.register(Category)
class CategoriesAdmin(DjangoMpttAdmin):
    fields = ('name', 'parent', 'image', 'position')
    list_display = ('id', 'name', 'parent', 'position', 'level')
    list_display_links = list_display
    list_filter = ('level',)
    search_fields = ('name',)


class ValueInLine(admin.TabularInline):
    model = Value
    extra = 1


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_values', 'category', 'position', 'price', 'code', 'is_available',)
    fieldsets = (
        (None, {
            "fields": ('name', 'name_values', 'price', 'category', 'position', 'code', 'is_available',)
        }),
        # ("Дополнительно", {
        #     'classes': ('collapse',),
        #     "fields": ('description',)
        # }),
        ("Изображение", {
            'classes': ('collapse',),
            "fields": ('image',)
        }),
    )
    list_display_links = list_display
    search_fields = ('code', 'name', 'position')
    list_filter = ('is_available', 'name', 'image')
    ordering = ('-id', 'position')
    readonly_fields = ['code', 'name_values']
    save_as = True
    save_on_top = True
    inlines = (ValueInLine,)



