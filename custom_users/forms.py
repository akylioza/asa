from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VipClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VipClient, 'VipClient'),
    (CLIENT, 'CLIENT')
)

MALE = 1
FEMALE = 2

GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)
# married; divorced, separated, or widowed; and never married
MARRIED = 1
DIVORCED = 2
WIDOWED = 3
Never_Married = 4

MARITAL = (
    (MARRIED, 'MARRIED'),
    (DIVORCED, 'DIVORCED'),
    (WIDOWED, 'WIDOWED'),
    (Never_Married, 'Never Married')
)

ELF = 1
HUMAN = 2
ORC = 3
TROLL = 4
GNOLL = 5
UNICORN = 6

RACES = (
    (ELF, 'ELF'),
    (HUMAN, 'HUMAN'),
    (ORC, 'ORC'),
    (TROLL, 'TROLL'),
    (GNOLL, 'GNOLL'),
    (UNICORN, 'UNICORN')
)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type= forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    marital_status = forms.ChoiceField(choices=MARITAL, required=True)
    race = forms.ChoiceField(choices=RACES, required=True)
    salary = forms.IntegerField(required=True)

    class Meta:
        model = models.Custom_User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'marital_status',
            'race',
            'salary'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
            'id': 'hello'

        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placholder': 'password',
            'id': 'hi'
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'email',
            'id': 'ola'
        }
    ))