from django import forms
from django.contrib.auth.models import User
# from .models import UserProfileInfo


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)
    def __str__(self):
        return self.name
    

# PASSWORD HASH

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = User
#         fields = ("username","email","password")
# class UserProfileForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site','profile_pic')