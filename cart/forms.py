# -*- coding: utf-8 -*-
from django import forms
from supercaptcha import CaptchaField

class OrderForm(forms.Form):
    fio = forms.CharField(label=u'Ваше имя')
    phones = forms.CharField(label=u'Контактный телефон', required=False)
    email = forms.EmailField(label=u'E-mail')
    comment = forms.CharField(label=u'Комментарий', widget=forms.Textarea, required=False)
    captcha = CaptchaField(label=u'Защита от роботов')