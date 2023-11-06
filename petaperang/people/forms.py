from django import forms

from people.models import Person


# Форма представления/редактирования человека
class IntroducingPersonForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    biography = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Биография'}))

    class Meta:
        model = Person
        fields = ['photo', 'name', 'biography', 'searchfield', 'events']
        widgets = {'searchfield': forms.HiddenInput()}


# Форма поисковика человека
class SearchingPersonalityForm(forms.Form):
    search_engine = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={'type': "text", 'name': "Input", 'id': "input_4914859299010", 'class': "t-input js-tilda-rule ",
               'value': "",
               'placeholder': "Имя Человека",
               'aria-describedby': "error_4914859299010",
               'style': "color:#000000;border:1px solid #000000;"}))
