# -*- coding: utf-8 -*-
import datetime

from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ('work', u'в работе'),
        ('done', u'готово'),
        ('cancel', u'отмена'),
    )
    status = models.CharField(u'Статус', choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0], max_length=20)
    fio = models.CharField(u'Имя', max_length=255)
    address = models.CharField(u'Адрес', max_length=255)
    phones = models.CharField(u'Телефон', max_length=255)
    email = models.CharField(u'Email', max_length=255, blank=True, null=True)
    comment =  models.TextField(u'Комментарий')
    dt_mod = models.DateTimeField(u'Дата заказа', default=datetime.datetime.now)
    
    def __unicode__(self):
        try:
            return u'заявка №%d' % self.pk
        except:
            return u'заявка'
    
    @property
    def sum_order(self):
        return sum([item['price'] or 0 * item['amount'] or 0 \
                   for item in self.items.values('price', 'amount')])
    
    def get_sum_order(self):
        return self.sum_order
    get_sum_order.short_description = u'Сумма заказа'
    
    def get_item_count(self):
        return self.items.count()
    get_item_count.short_description = u'Позиций в заказе'
    
    def get_dt_mod(self):
        from django.utils.dateformat import format
        return  format(self.dt_mod, 'd E Y H:i')
    get_dt_mod.short_description = u'Дата заказа'
    
    class Meta:
        ordering = ('-id', )
        verbose_name = u'заявка'
        verbose_name_plural = u'заявки'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=u'заявка', related_name='items')
    description = models.TextField(u'Описание заказа')
    insertions = models.TextField(u'Вставки', blank=True, null=True,)
    amount = models.PositiveIntegerField(u'Количество товаров')
    size = models.CharField(u'Размер', max_length=255, blank=True, null=True)
    weight = models.CharField(u'Вес', max_length=255, blank=True, null=True)
    barcode = models.CharField(u'Штрих код', max_length=255, blank=True, null=True)
    
    price = models.DecimalField(u'Цена за единицу', blank=True, null=True,
        max_digits=10, decimal_places=2)
    @property
    def sum_price(self):
        return self.price * self.amount
    def get_sum_price(self):
        return self.sum_price
    get_sum_price.short_description = u'Итого'
    
    def __unicode__(self):
        return u'товар в заявке'
    
    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = u'товары в заявке'
