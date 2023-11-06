from django import forms

from maps.models import Event, LocalMap


# Форма для создания/редактирования события
class IntroducingEventForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    begin = forms.DateField(label='Начало', widget=forms.DateInput(attrs={'type': 'date'}))
    end = forms.DateField(label='Конец', widget=forms.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Описание'}))
    x = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'точка x'}))
    y = forms.FloatField( widget=forms.NumberInput(attrs={'placeholder': 'точка Y'}))
    zoom = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Зум карты'}))
    kml = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder': 'URL-адрес KML файла'}))

    class Meta:
        model = Event
        fields = ['name', 'begin', 'end', 'description', 'x', 'y', 'kml', 'zoom', 'searchfield']
        widgets = {'searchfield': forms.HiddenInput()}


# форма для создания/редактирования локальной карты
class LocalMapCreatorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Описание'}))
    url = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder': 'URL адрес на доп материал'}))
    x = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'точка x'}))
    y = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'точка Y'}))

    class Meta:
        model = LocalMap
        fields = ['name', 'description', 'small_map', 'event_link', 'x', 'y']
