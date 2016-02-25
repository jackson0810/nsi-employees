from django import forms
from django.forms import ModelForm


from shared.models import NewsItem, FunctionalCapability, ImageItem
from shared.forms import RadioSelectInline


class NewsItemForm(ModelForm):
    bool_choices = ((True, 'Yes'), (False, 'No'))

    #featured = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=False)

    class Meta:
        model = NewsItem
        fields = ['featured', 'title', 'text']
