from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

from image_quality_tagging import onetimeload

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'analytics.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^image_quality_tagging/',
                           include('image_quality_tagging.urls')),

                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
