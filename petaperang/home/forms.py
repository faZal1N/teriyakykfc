from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from home.models import User


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(label="+7 (999) 999-99-99", max_length=12, required=True,
                                   widget=forms.TextInput(attrs={'type': "tel",
                                                                 'autocomplete': "tel",
                                                                 'class': "t-input",
                                                                 'placeholder': "+7 (999) 999-99 99",
                                                                 'maxlength': 12,
                                                                 'style': "color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;"}))
    username = forms.CharField(label="Login", required=True, widget=forms.TextInput(attrs={'type': "text",
                                                                                           'id': "input_8571215261582",
                                                                                           'class': "t-input",
                                                                                           'placeholder': 'Login',
                                                                                           'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))
    password1 = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'type': "text",
                                                                                                   'id': "input_8571215261582",
                                                                                                   'class': "t-input",
                                                                                                   'placeholder': 'Password',
                                                                                                   'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))
    password2 = forms.CharField(label="Repeat password", required=True,
                                widget=forms.PasswordInput(attrs={'type': "text",
                                                                  'id': "input_8571215261582",
                                                                  'class': "t-input",
                                                                  'placeholder': 'Repeat Password',
                                                                  'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))
    email = forms.CharField(label="Repeat password", required=True,
                                widget=forms.TextInput(attrs={'type': "email",
                                                                  'id': "input_8571215261582",
                                                                  'class': "t-input",
                                                                  'placeholder': 'Email',
                                                                  'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))


    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')



class RegEditorForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", required=True,
                                 widget=forms.TextInput(attrs={'type': "text",
                                                               'autocomplete': "first_name",
                                                               'class': "t-input",
                                                               'placeholder': "Имя",
                                                               'style': "color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;"}))
    second_name = forms.CharField(label="Фамилия", required=True,
                                  widget=forms.TextInput(attrs={'type': "text",
                                                                'autocomplete': "second_name",
                                                                'class': "t-input",
                                                                'placeholder': "Фамилия",
                                                                'style': "color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;"}))

    editor_rights = forms.BooleanField(widget=forms.CheckboxInput(attrs={'label': 'Права редактора', 'class': " t-checkbox__indicator"}))

    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'editor_rights')


class AllUpdateForm(forms.ModelForm):
    phone_number = forms.CharField(label="+7 (999) 999-99-99", max_length=12, required=True,
                                   widget=forms.TextInput(attrs={'type': "tel",
                                                                 'autocomplete': "tel",
                                                                 'class': "t-input",
                                                                 'placeholder': "+7 (999) 999-99 99",
                                                                 'maxlength': 12,
                                                                 'style': "color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;"}))
    password1 = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'type': "text",
                                                                                                   'id': "input_8571215261582",
                                                                                                   'class': "t-input",
                                                                                                   'placeholder': 'Password',
                                                                                                   'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))
    password2 = forms.CharField(label="Repeat password", required=True,
                                widget=forms.PasswordInput(attrs={'type': "text",
                                                                  'id': "input_8571215261582",
                                                                  'class': "t-input",
                                                                  'placeholder': 'Repeat Password',
                                                                  'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))
    email = forms.CharField(label="Repeat password", required=True,
                            widget=forms.TextInput(attrs={'type': "email",
                                                          'id': "input_8571215261582",
                                                          'class': "t-input",
                                                          'placeholder': 'Email',
                                                          'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))


    first_name = forms.CharField(label="Имя",  required=True,
                                       widget=forms.TextInput(attrs={'type': "text",
                                                                     'autocomplete': "first_name",
                                                                     'class': "t-input",
                                                                     'placeholder': "Имя",
                                                                     'style': "color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;"}))
    second_name = forms.CharField(label="Фамилия",  required=True,
                                       widget=forms.TextInput(attrs={'type': "text",
                                                                     'autocomplete': "second_name",
                                                                     'class': "t-input",
                                                                     'placeholder': "Фамилия",
                                                                     'style': "color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;"}))

    class Meta:
       model = User
       fields = ('phone_number', 'email', 'password1', 'password2', 'first_name', 'second_name')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", required=True, widget=forms.TextInput(
        attrs={'type': "text", 'class': "t-input ",
               'placeholder': "Login", 'data-tilda-req': "1", 'aria-required': "true",
               'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'
               }))

    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(
        attrs={'type': "password", 'class': "t-input ",
               'placeholder': "Password", 'data-tilda-req': "1", 'aria-required': "true",
               'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'
               }))


class UserUpdateInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'second_name', 'phone_number']


class RequestForEditingRightForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'second_name']


class EmailConfirmation(forms.ModelForm):
    email = forms.CharField(label="Repeat password", required=True,
                            widget=forms.TextInput(attrs={'type': "email",
                                                          'id': "input_8571215261582",
                                                          'class': "t-input",
                                                          'placeholder': 'Email',
                                                          'style': 'color:#000000;background-color:#ffffff;border-radius: 7px; -moz-border-radius: 7px; -webkit-border-radius: 7px;'}))

    class Meta:
        model = User
        fields = ['email']
