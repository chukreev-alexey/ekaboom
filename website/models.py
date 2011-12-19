# -*- coding: utf-8 -*-
import datetime


from django.contrib.contenttypes import generic
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from common.fields import MultiEmailField
from filebrowser.fields import FileBrowseField
from tinymce import models as tinymce_models

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^common\.fields\.MultiEmailField"])

from gallery.models import Gallery

class VisibleObjects(models.Manager):
    def get_query_set(self):
        return super(VisibleObjects, self).get_query_set().filter(visible=True)

class Settings(models.Model):
    project = models.CharField(u'Название проекта', max_length=255)
    email = MultiEmailField(u'Email для писем', max_length=255,
        help_text=u'''Можете вставить несколько email, разделив их запятой''')
    
    def __unicode__(self):
        return u'настройки'
            
    class Meta:
        verbose_name = u'настройки'
        verbose_name_plural = u'настройки'

@receiver(post_save, sender=Settings)
@receiver(post_delete, sender=Settings)
def clear_settings_cache(sender, **kwargs):
    cache.delete('settings')

class News(models.Model):
    name = models.CharField(u'Заголовок', max_length=255)
    image = FileBrowseField(u"Фото", format='Image', max_length=255,
                            blank=True, null=True)
    dt_mod = models.DateField(u'Дата новости', default=datetime.date.today)
    preview = models.TextField(u'Краткое описание')
    content = tinymce_models.HTMLField(u'Текст новости', blank=True, null=True)
    visible = models.BooleanField(u'Показывать', default=False)
    
    allobjects = models.Manager()
    objects = VisibleObjects()
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ('-dt_mod', '-id')
        verbose_name = u'новость'
        verbose_name_plural = u'новости'    

class Author(models.Model):
    name = models.CharField(u'ФИО автора', max_length=100)
    
    def __unicode__(self):
        return self.name
            
    class Meta:
        ordering = ('name', )
        verbose_name = u'автор'
        verbose_name_plural = u'авторы'
        
class Category(models.Model):
    name = models.CharField(u'Название', max_length=100)
    url = models.CharField(u'Адрес', max_length=100, unique=True)
    image = FileBrowseField(u"Фото", format='Image', max_length=255)
    sort = models.IntegerField(u'Порядок', default=0)
    visible = models.BooleanField(u'Показывать', default=False)
    
    allobjects = models.Manager()
    objects = VisibleObjects()
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category': self.url})
    
    class Meta:
        ordering = ('sort', )
        verbose_name = u'категория'
        verbose_name_plural = u'категории товаров'

class Product(models.Model):
    name = models.CharField(u'Название', max_length=255)
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    author = models.ForeignKey(Author, verbose_name=u'Автор')
    materials = tinymce_models.HTMLField(u'Материалы', blank=True, null=True)
    content = tinymce_models.HTMLField(u'Описание', blank=True, null=True)
    gallery = generic.GenericRelation(Gallery, verbose_name=u'Фотогалерея')
    sort = models.IntegerField(u'Порядок', default=0)
    visible = models.BooleanField(u'Показывать', default=False)
    
    allobjects = models.Manager()
    objects = VisibleObjects()
    
    def __unicode__(self):
        return self.name
            
    class Meta:
        ordering = ('sort', )
        verbose_name = u'товар'
        verbose_name_plural = u'товары'

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, verbose_name=u'Товар',
        related_name='prices')
    label = models.CharField(u'Ярлык', max_length=255)
    price = models.IntegerField(u'Цена')
    
    def __unicode__(self):
        return '%s %s %d' % (self.label, self.product.name, self.price)
            
    class Meta:
        verbose_name = u'цена'
        verbose_name_plural = u'цены товаров'
    
    