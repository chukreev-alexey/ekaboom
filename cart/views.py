# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from django.template import RequestContext
from django.template.loader import render_to_string
from django.db import transaction

from common.fields import emails_list
from cart import Cart
from cart.models import Order
from cart.forms import OrderForm


def show_cart(request):
    return render_to_response('cart.html', {},
        context_instance=RequestContext(request))

@transaction.commit_on_success
def order_cart(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            subject = u'Заказ с сайта'
            recipients = []
            try:
                recipients.extend(emails_list(request.settings.email))
            except:
                recipients.append(settings.ADMINS[0][1])
            cart = Cart(request, init=True)
            # Order insertion
            if cart.objects:
                order = Order.objects.create(fio=form.cleaned_data['fio'],
                                             address='',
                                             phones=form.cleaned_data['phones'],
                                             email=form.cleaned_data['email'],
                                             comment=form.cleaned_data['comment'])
                for item in cart.objects:
                    order.items.create(label=item.label,
                                       amount=item.amount,
                                       price=item.price)
            subject = u'Поступил заказ с сайта %s' % settings.PROJECT_TITLE
            letter_context = form.cleaned_data
            letter_context.update({'site': settings.PROJECT_TITLE,
                                   'cart': cart, 'subject': subject})
            
            text_content = render_to_string('letters/order_text.txt', letter_context)
            html_content = render_to_string('letters/order_html.html', letter_context)
            
            msg = EmailMultiAlternatives(subject, text_content,
                recipients[0], recipients)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            cart.delete_all()
            success_message = request.infoblock.get('order_send_message', u"""
            Благодарим за то, что Вы воспользовались услугами нашего Интернет-магазина.
            Ваша заявка принята в обработку, и наш менеджер свяжется с Вами в ближайшее время для уточнения деталей.
            """)
            messages.add_message(request, messages.SUCCESS, success_message)
            return redirect(reverse('message_list'))
    else:
        form = OrderForm()
    return render_to_response('cart_order.html', {'form': form},
        context_instance=RequestContext(request))   
        
def add_cart(request):
    cart = Cart(request)
    product = int(request.POST.get('product', 0))
    if product > 0:
        request = cart.add(product)
    return HttpResponse(cart.serialize())
    
def update_cart(request):
    cart = Cart(request)
    product = int(request.POST.get('product', '0'))
    amount = int(request.POST.get('amount', '0'))
    i = int(request.POST.get('i', '0'))
    data = None
    
    if product > 0 and amount >= 0:
        if amount == 0:
            cart.delete(product)
        else:
            cart.update({'product': product, 'amount': amount})
        return HttpResponse(cart.serialize())
    else:
        raise Http404

def delete_cart(request, id):
    cart = Cart(request)
    cart.delete(id)
    if request.META.get('HTTP_X_REQUESTED_WITH', '') == 'XMLHttpRequest':
        return HttpResponse(cart.serialize())
    else:
        return redirect(reverse('show_cart'))

def empty_cart(request):
    cart = Cart(request)
    cart.delete_all()
    return redirect('/') 