from django import forms
from django.forms import ModelForm


from shared.models import NewsItem, FunctionalCapability, ImageItem
from shared.forms import RadioSelectInline


class NewsItemForm(ModelForm):
    bool_choices = ((True, 'Yes'), (False, 'No'))

    is_active = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)

    class Meta:
        model = NewsItem
        fields = ['featured', 'title', 'text', 'is_active']


class FunctionalCapabilityForm(ModelForm):
    bool_choices = ((True, 'Yes'), (False, 'No'))

    is_active = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)

    class Meta:
        model = FunctionalCapability
        fields = ['title', 'text', 'is_active']
