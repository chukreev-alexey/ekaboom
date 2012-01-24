# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from common.fields import emails_list

from website.models import Product, Category, News

def page(request, page_url):
    template = 'base.html'
    context = {'news_list': News.objects.all()[:3]}
    return render(request, template, context)

def category_detail(request, category):
    category = get_object_or_404(Category, url=category)
    return render(request, 'category_detail.html',
        {'category': category, 'product_list': Product.objects.filter(category=category)})

def catalog(request):
    return render(request, 'catalog.html',
        {'object_list': Category.objects.all()})
    
def message_list(request, arg=None):
    return render(request, 'messages.html')
        
def feedback(request):
    from website.forms import FeedbackForm
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = u'Вопрос с сайта'
            recipients = []
            recipients.extend(emails_list(request.settings.email))
            letter_context = form.cleaned_data
            letter_context.update({'site': request.settings.project})
            letter_content = render_to_string('feedback_letter.txt', letter_context)
            send_mail(subject, letter_content,
                      letter_context['email'] or recipients[0], recipients)
            messages.add_message(request, messages.SUCCESS, u"Ваше письмо успешно отправлено администрации сайта.")
            return redirect(reverse('message_list'))
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})