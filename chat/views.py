#-*- coding: utf-8 -*-
# Create your views here.
from chat.forms import ConnexionForm, AddMessageForm
from chat.models import Message
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

 
def home(request):
    return render(request, 'home.html', {'current_date': datetime.now()})

def add_message(request):
    if request.user.is_authenticated(): 
        if request.method == "POST":
            form_message = AddMessageForm(request.POST)
            if form_message.is_valid():
                user_me=User.objects.get(username__exact=request.user.username)
                
                mess= Message()
                mess.contenu=form_message.cleaned_data["message"]
                mess.auteur=user_me
                mess.date=timezone.now()
            
                mess.save()
        else:
            form_message = AddMessageForm()
    return redirect(reverse(connexion))



def check_messages_ajax(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            last_message_id = request.POST.get('last_message_id', '')
            message_list=Message.objects.filter(pk__gt=last_message_id).order_by('date')[:10]
            data = serializers.serialize('json', message_list, use_natural_keys=True) 
            return HttpResponse(data)
# encode json

#    return redirect('/')

def connexion(request):
    error = False
    if request.user.is_authenticated():   
        #request.user
        #raise SystemExit
        user_me=User.objects.get(username__exact=request.user.username)
        user_me.last_login=timezone.now()
        user_me.save()
        
        temp_date = timezone.now()
        # on enleve 10 min
        temp_date= temp_date- timezone.timedelta(0, 10 * 60)
        
        #return HttpResponse(d)
        
        #raise SystemExit
        message_list=Message.objects.order_by('date')[:10]    
        user_connected= User.objects.filter(last_login__gte= temp_date)
        
    else:
        if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
                password = form.cleaned_data["password"]  # … et le mot de passe
                user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
                if user:  # Si l'objet renvoyé n'est pas None
                    login(request, user)  # nous connectons l'utilisateur
                    return redirect(reverse(connexion))
                else: #sinon une erreur sera affichée
                    error = True
        else:
            form = ConnexionForm()
    form_message = AddMessageForm()
 
        
 
    return render(request, 'connexion.html',locals())


def deconnexion(request):                                                                               
    logout(request)                                                                                     
    return redirect(reverse(connexion))