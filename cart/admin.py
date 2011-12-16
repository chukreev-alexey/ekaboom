# -*- coding: utf-8 -*-
from django.contrib import admin
from cart.models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = [field.name for field in OrderItem._meta.fields
                                  if field.name.lower()!='id'] + ['get_sum_price']
    can_delete = False
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'address', 'get_item_count', 'get_sum_order', 'get_dt_mod')
    readonly_fields = list(set([field.name for field in Order._meta.fields if field.name.lower()!='id']) - set(['status']))
    list_filter = ('status', )
    inlines = [OrderItemInline]
admin.site.register(Order, OrderAdmin)