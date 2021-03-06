from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from moments.api import ABOINGA_API
from moments.models import MomentSitemap
from os import path
admin.autodiscover()

sitemaps ={
    "moments": MomentSitemap
}

urlpatterns = patterns('',
    (r'^(favicon.ico)', 'django.views.static.serve',
        {'document_root' : path.join(settings.ROOT_PATH, 'static', 'img')}),
    (r'^(robots.txt)', 'django.views.static.serve',
        {'document_root' : path.join(settings.ROOT_PATH, 'static')}),
    (r'^(humans.txt)', 'django.views.static.serve',
        {'document_root' : path.join(settings.ROOT_PATH, 'static')}),
    (r'^(google.*.html)', 'django.views.static.serve',
        {'document_root' : path.join(settings.ROOT_PATH, 'static')}),
    (r'^user_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': path.join(settings.ROOT_PATH, 'user_media')}),

    url(r'^internal_admin/', include(admin.site.urls)),

    (r'^api/', include(ABOINGA_API.urls)),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    url(r'', include('aboinga_web.moments.urls')),

)
