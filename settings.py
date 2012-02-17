# -*- coding: utf-8 -*-
import os, sys

from local_settings import *

MY_DJANGO_ROOT = os.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.sep)[:-2])
sys.path.append(MY_DJANGO_ROOT)
sys.path.append(MY_DJANGO_ROOT+'/apps')
sys.path.append(PROJECT_DIR)

from common.settings import *

SITE_ID=1

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_DIR + '/media/'

STATIC_URL = MEDIA_URL
STATIC_ROOT = MEDIA_ROOT

ADMIN_MEDIA_PREFIX = '/admin_media/'
ADMIN_MEDIA_ROOT = MY_DJANGO_ROOT + '/admin_media/'

SECRET_KEY = '8!&d=_!md4nzvv0i658(vnyzdfdf_)-@b39g$_0+-oer3s0872'

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

TEMPLATE_DIRS = (
    PROJECT_DIR + "/website/templates",
    MY_DJANGO_ROOT + "/apps/common/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sites',
    'common',
    'filebrowser',
    'tinymce',
    'mptt',
    'treeadmin',
    'south',
    'sorl.thumbnail',
    'watermarker',
    'seo',
    'gallery',
    'cart',
    'pages',
    'website',
)

# THUMBNAIL
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
THUMBNAIL_DEBUG = False

# MESSAGES
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# FILEBROWSER
FILEBROWSER_URL_FILEBROWSER_MEDIA = os.path.join(ADMIN_MEDIA_PREFIX , 'filebrowser/')
FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(ADMIN_MEDIA_ROOT , 'filebrowser/')
FILEBROWSER_URL_TINYMCE = os.path.join(ADMIN_MEDIA_PREFIX , 'tiny_mce/')
FILEBROWSER_PATH_TINYMCE = os.path.join(ADMIN_MEDIA_ROOT , 'tiny_mce/')

FILEBROWSER_VERSIONS_BASEDIR = '_versions_'
FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 40, 'height': 40, 'opts': 'upscale'},
    'fancybox': {'verbose_name': 'FancyBox image', 'width': 700, 'height': '', 'opts': 'upscale'},
    'category_small': {'verbose_name': u'Для списка категорий', 'width': 67, 'height': 90, 'opts': 'upscale'},
    'category_index_list': {'verbose_name': u'Для списка категорий', 'width': 120, 'height': 200, 'opts': 'upscale'},
    'product_small': {'verbose_name': u'Маленькая для карточки товаров', 'width': 60, 'height': '', 'opts': 'upscale'},
    'product_big': {'verbose_name': u'Большая для карточки товаров', 'width': 180, 'height': '', 'opts': 'upscale'},
}
FILEBROWSER_ADMIN_VERSIONS = ['fb_thumb']
FILEBROWSER_ADMIN_THUMBNAIL ='fb_thumb'

# CAPTCHA SETTINGS
CAPTCHA_CACHE_PREFIX = PROJECT_NAME+"_captcha_"
CAPTCHA_HTML_TEMPLATE_WITH_REFRESH = u"""
<div class="CaptchaBlock">
    <div class="Captcha">
        <img id="captcha_field_image" src="%(src)s?%(rnd)s" alt="%(alt)s" width="%(width)s" height="%(height)s"/><br />
        <a onclick="var img=document.getElementById('captcha_field_image'); img.src=img.src.substring(0,img.src.indexOf('?')+1)+Math.random();return false;" href="#refresh">Неразборчиво?</a>
    </div>
    <div class="CaptchaInput">
        <input%(input_attrs)s maxlength="%(length)s" />
    </div>
</div>
"""


# TINYMCE SETTINGS
TINYMCE_JS_ROOT = os.path.join(ADMIN_MEDIA_ROOT, 'tiny_mce')
TINYMCE_JS_URL = os.path.join(ADMIN_MEDIA_PREFIX, 'tiny_mce/tiny_mce.js')
