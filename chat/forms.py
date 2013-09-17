#-*- coding: utf-8 -*-
from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="",max_length=30,widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Login"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control',"placeholder":"Pasword"}))
    
class AddMessageForm(forms.Form):
    message = forms.CharField(label="",max_length=300,widget=forms.Textarea(attrs={'class':'form-control',"placeholder":"Write a message","rows":"3"}))
    
    
