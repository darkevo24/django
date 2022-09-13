from django.forms import ModelForm
from .models import User
from django import forms
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
      'password': forms.PasswordInput()
         }
