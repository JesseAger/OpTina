from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    firstname= forms.CharField( max_length=100, required=True)
    lastname= forms.CharField(max_length=100, required=False)
    phone_number= forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields=('firstname', 'lastname', 'phonenumber', 'email', 'username', 'password1', 'password2')
        class CustomSignUpForm(UserCreationForm):

            def save(self, commit=True):
                user = super().save(commit=False)
                user.email = self.cleaned_data["email"]
                user.firstname = self.cleaned_data["firstname"]
                user.lastname = self.cleaned_data["lastname"]
                if commit:
                    user.save()
                return user