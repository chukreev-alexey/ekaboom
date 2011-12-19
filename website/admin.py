# -*- coding: utf-8 -*-
from django.contrib import admin

from website.models import (Settings, Category, Author, Product, ProductPrice,
                            News)
from gallery.admin import GalleryInline

admin.site.register(Settings)
admin.site.register(News)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'sort', 'visible')
    list_editable = ('image', 'sort', 'visible')
admin.site.register(Category, CategoryAdmin)

admin.site.register(Author)

class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'sort', 'visible')
    list_editable = ('sort', 'visible')
    list_filter = ('visible', 'category', 'author')
    search_fields = ('name', 'author__name')
    inlines = (GalleryInline, ProductPriceInline)
admin.site.register(Product, ProductAdmin)
