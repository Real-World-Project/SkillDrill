from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(services, cart):
    keys = cart.keys()
    for id in keys:
        if id == str(services.id):
            return True
    return False;

@register.filter(name='cart_quantity')
def cart_quantity(services, cart):
    keys = cart.keys()
    for id in keys:
        if id == str(services.id):
            return cart.get(id)
    return 0;

@register.filter(name='price_total')
def price_total(services, cart):
    return services.charge * cart_quantity(services, cart)

@register.filter(name="total_cart_price")
def total_cart_price(services, cart):
    sum = 0;
    for s in services:
        sum += price_total(s, cart)
    return sum
