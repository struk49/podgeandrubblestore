from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    templates = 'checkout/checkout1.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51O2vtYG3G7lKiCY618POHC66h3gueThdXnUmbcyOWX3pJn4uPBXUZwEklFZjAv8Vteo6erMlUPYDvpujVZsrgl0L00VUPQAw6c',
        'client_secret': 'test client secret',
    }

    return render(request, templates, context)