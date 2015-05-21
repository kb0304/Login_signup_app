from django.conf.urls import patterns, url
from ag53 import views

urlpatterns = patterns('',
    url(r'^$', views.ag53_home_view, name='ag53_home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'ag53/login.html'}),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^profile/logout$', views.logout_view, name='logout_url')
)
