from django import forms
from django.forms import ModelForm


from shared.models import NewsItem, FunctionalCapability, ImageItem, TaskOrder, FormData, FormCategory
from shared.forms import RadioSelectInline, CheckboxSelectInline


class NewsItemForm(ModelForm):
    bool_choices = ((True, 'Yes'), (False, 'No'))
    year_choices = [('', 'Select year...'), ]

    for x in range(2012, 2100):
        year_choices.append((x, x))

    is_active = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)
    news_year = forms.ChoiceField(choices=year_choices)

    class Meta:
        model = NewsItem
        fields = ['featured', 'title', 'text', 'is_active', 'news_year']


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


class FormDataForm(ModelForm):
    def __init__(self, *args, **kwargs):

        super(FormDataForm, self).__init__(*args, **kwargs)

        bool_choices = ((True, 'Yes'), (False, 'No'))
        data_type_choices = (('form', 'Form'), ('link', 'Link'))

        self.fields['is_active'] = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)
        self.fields['data_type'] = forms.ChoiceField(choices=data_type_choices, initial='form')

    def clean(self):
        cleaned_data = super(FormDataForm, self).clean()
        data_type = cleaned_data.get('data_type')

        if data_type == 'form' and not cleaned_data.get('document'):
            self._errors['document'] = self.error_class('Please choose the form you would like to upload.')
        elif data_type == 'link' and not cleaned_data.get('link'):
            self._errors['link'] = self.error_class('A valid link is required')

    class Meta:
        model = FormData
        fields = ['title', 'document', 'is_active', 'category', 'data_type', 'link']


class FomCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):

        super(FomCategoryForm, self).__init__(*args, **kwargs)

        bool_choices = ((True, 'Yes'), (False, 'No'))

        self.fields['is_active'] = forms.ChoiceField(choices=bool_choices, widget=RadioSelectInline, initial=True)

    class Meta:
        model = FormCategory
        fields = ['category', 'is_active']
