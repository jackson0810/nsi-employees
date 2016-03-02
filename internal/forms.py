from django import forms
from django.forms import ModelForm


from shared.models import NewsItem, FunctionalCapability, ImageItem, TaskOrder
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


class TaskOrderForm(ModelForm):
    def __init__(self, *args, **kwargs):

        super(TaskOrderForm, self).__init__(*args, **kwargs)

        bool_choices = ((True, 'Yes'), (False, 'No'))

        self.fields['is_active'] = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)
        self.fields['document'].required = False

    class Meta:
        model = TaskOrder
        fields = ['task_number', 'document', 'is_active']


class ImageItemForm(ModelForm):
    def __init__(self, *args, **kwargs):

        super(ImageItemForm, self).__init__(*args, **kwargs)

        bool_choices = ((True, 'Yes'), (False, 'No'))

        self.fields['is_active'] = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)
        self.fields['featured'] = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)

    class Meta:
        model = ImageItem
        fields = ['title', 'text', 'image', 'is_active', 'featured']
