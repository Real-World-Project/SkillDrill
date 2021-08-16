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
