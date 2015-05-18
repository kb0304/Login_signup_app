from django.conf.urls import patterns, url
from ag53 import views

urlpatterns = patterns('', url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'ag53/login.html'}),
    url(r'^profile/$', views.profile_view, name='profile'),
)
