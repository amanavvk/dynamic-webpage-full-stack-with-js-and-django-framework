from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core import validators


class Createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class Formname(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    #def clean_botcatcher(self):
        #botcatcher=self.cleaned_data['botcatcher']
        #if len(botcatcher)>0:
            #raise forms.ValidationError("gotcha bot!")
            #return botcatcher
