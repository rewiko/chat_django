#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
 
class Message(models.Model):
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de création")
    auteur = models.ForeignKey(User)
    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
        return u"%s" % self.contenu
    
  
    
   
