from django.conf.urls import patterns, url
from ag53 import views

urlpatterns = patterns('',
    url(r'^$', views.ag53_home_view, name='ag53_home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'ag53/login.html'}),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout$', views.logout_view, name='logout_url'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',{'post_change_redirect' : '/ag53/cpsuccess'},name="password_change"), 
    url(r'^cpsuccess$', views.cpsuccess,name='cpsuccess'),


)
