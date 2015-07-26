from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from mysite import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^ag53/', include('ag53.urls')),

    url(r'^admin/', include(admin.site.urls)),
) +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
