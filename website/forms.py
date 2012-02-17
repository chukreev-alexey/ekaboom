# -*- coding: utf-8 -*-
from django import forms
from supercaptcha import CaptchaField

from .models import Author

def as_eul(self):
    return self._html_output(
        normal_row = u'<li%(html_class_attr)s><div class="FormLabel">%(label)s</div> <div class="FormField">%(field)s</div><div class="FormError">%(errors)s</div><div class="FormHelpText">%(help_text)s</div></li>',
        error_row = u'<li>%s</li>',
        row_ender = '</li>',
        help_text_html = u' %s',
        errors_on_separate_row = False)
forms.BaseForm.as_eul = as_eul

class FeedbackForm(forms.Form):
    fio = forms.CharField(label=u'Ваше имя')
    phones = forms.CharField(label=u'Контактный телефон', required=False)
    email = forms.EmailField(label=u'Email')
    comment = forms.CharField(label=u'Комментарий', widget=forms.Textarea)
    captcha = CaptchaField(label=u'Защита от роботов')

class FilterForm(forms.Form):
    query = forms.CharField(label=u'Название', required=False)
    author = forms.ModelChoiceField(label=u'Авторы', required=False,
        queryset=Author.objects.all(), empty_label=' -- ')
    