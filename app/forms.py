
from django import forms
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm,AuthenticationForm
class PasswordReset(PasswordResetForm):
    email=forms.EmailField(label=('Email'),max_length=200,
                           widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control','placeholder':'enter your e-mail'}))

class Passwordconfirm(SetPasswordForm):
    newpassword=forms.CharField(label=('New Password'),widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
                                                                  'placeholder':'Enter your newpassword','class':'form-control'}))
    password2=forms.CharField(label=('Confirm Password'),widget=forms.PasswordInput(attrs={'autocomplete':'confirm-password',
                                                                  'placeholder':'Confirm-Password','class':'form-control'}))
    

    
    
    