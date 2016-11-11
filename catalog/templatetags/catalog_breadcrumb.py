from django import template

register = template.Library()


@register.inclusion_tag('template_tags/breadcrumbs.html')
def catalog_breadcrumb(category, product=None):
    return {
        'category': category,
        'product': product
    }