#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import ListView
from chat.models import Message
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'init_django.views.home', name='home'),
    # url(r'^init_django/', include('init_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   
    url(r'^chat/', include('chat.urls')),
    url(r'^$', include('chat.urls')),
    url(r'^faq/', TemplateView.as_view(template_name='faq.html')),
 
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
  
)
