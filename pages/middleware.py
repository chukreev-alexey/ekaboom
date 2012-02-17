# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.conf import settings
from pages.models import Page, InfoBlock
from website.models import Settings, Category, News
from cart import Cart

class PageMiddleware(object):
    """
    Add page object to request objec
    """
    def __init__(self):
        pass

    def common_actions(self, request):
        request.settings = cache.get('settings')
        if not request.settings:
            try:
                request.settings = Settings.objects.all()[0]
                cache.set('settings', request.settings, 60*60*24)
            except:
                pass

        request.infoblock = cache.get('infoblock')
        if not request.infoblock:
            try:
                request.infoblock = dict(
                    [(item.name, item.content_text or item.content_html) \
                     for item in InfoBlock.objects.all()])
                cache.set('infoblock', request.infoblock, 60*60*24)
            except:
                pass
        return request
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.PROJECT_TITLE = settings.PROJECT_TITLE
        if not view_func.__module__ in ('website.views', 'cart.views'):
            return None

        url = "/".join(filter(lambda x: bool(x), request.path_info.split('/')))

        request = self.common_actions(request)
        request.top_menu = list(Page.objects.filter(pk=1)) + list(Page.objects.filter(level=1))
        request.category_menu = Category.objects.all()
        request.cart = Cart(request, init=True)

        try:
            page = Page.objects.get(path=url)
            request.page = page
        except Page.DoesNotExist:
            if view_func.__name__ == 'page':
                raise Http404
            else:
                request.page = Page()
        if request.page.redirect_to and not request.page.redirect_to.redirect_to:
            return HttpResponseRedirect(request.page.redirect_to.get_absolute_url() or '/')
        request.ancestors = list(request.page.get_ancestors()) + [request.page]
        request.news_list = News.objects.all()[:3]
        return None
