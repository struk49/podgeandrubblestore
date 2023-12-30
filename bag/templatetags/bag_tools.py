from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(discount_price, quantity):
    return discount_price * quantity