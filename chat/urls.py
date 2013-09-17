# -*- coding: utf-8 -*-
from chat.models import Message
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.views.generic.list import ListView

# Uncomment the next two lines to enable the admin:
admin.autodiscover()
 
urlpatterns = patterns('chat.views',
    # Nous allons réécrire l'URL de l'accueil
    url(r'^check_messages_ajax', 'check_messages_ajax', name='check_messages_ajax'),
    url(r'^connexion/$', 'connexion', name='connexion'),
    url(r'^deconnexion/$', 'deconnexion', name='deconnexion'),
    url(r'^$', 'connexion', name='connexion'),
    url(r'^add_message', 'add_message', name='add_message'),
    
    
    
     url(r'^$', ListView.as_view(model=Message, context_object_name="derniers_messages",
                    template_name="message_list.html")),
    
      
)
