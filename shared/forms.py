from django import forms
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
from django.utils.html import conditional_escape


class RadioSelectInline(forms.RadioSelect):
    def render(self, *args, **kwargs):
        output = super(RadioSelectInline, self).render(*args, **kwargs)
        return mark_safe(output.replace(u'<ul', u'<ul class="unstyled" ').replace(u'<li>', u'').replace(u'</li>', u'').replace(u'<label ', u'<label class="radio inline" '))


class CheckboxSelectInline(forms.CheckboxSelectMultiple):
    def render(self, *args, **kwargs):
        output = super(CheckboxSelectInline, self).render(*args,**kwargs)
        return mark_safe(output.replace(u'<ul>', u'').replace(u'</ul>', u'').replace(u'<li>', u'').replace(u'</li>', u'').replace(u'<label ', u'<label class="checkbox inline" '))


class RadioSelectStacked(forms.RadioSelect):
    def render(self, *args, **kwargs):
        output = super(RadioSelectStacked, self).render(*args,**kwargs)
        return mark_safe(output.replace(u'<ul>', u'').replace(u'</ul>', u'').replace(u'<li>', u'').replace(u'</li>', u''))


class CustomCheckboxSelectMultipleIncomeTypeOnly(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        attrs['class'] = 'asset_income_type'
        final_attrs = self.build_attrs(attrs, name=name)
        output = []
        # Normalize to strings
        str_values = set([force_text(v) for v in value])
        counter = 1
        for i in self.choices.queryset:
            cb = forms.CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
            option_value = force_text(i.id)
            rendered_cb = cb.render(name, option_value)
            option_label = conditional_escape(force_text(i.name))
            if counter % 2 == 0:
                output.append('<div class="span7"><label class="checkbox inline">%s %s</label>' % (rendered_cb, option_label))
                #if i.id == 9:
                #    output.append('<input type="text" name="asset_income_other" id="id_asset_income_other" disabled="disabled" title="Specify other type." class="input-medium" placeholder="Specify other..." />')
                output.append('</div></div>')
            else:
                output.append('<div class="row-fluid"><div class="span5"><label class="checkbox inline">%s %s</label>' % (rendered_cb, option_label))
                #if i.id == 9:
                #    output.append('<input type="text" name="asset_income_other" id="id_asset_income_other" disabled="disabled" title="Specify other type." class="input-medium" placeholder="Specify other..." /></div>')
                output.append('</div>')

            counter += 1

        return mark_safe('\n'.join(output))


class CustomCheckboxSelectMultipleAccountType(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        attrs['class'] = 'asset_income_type'
        final_attrs = self.build_attrs(attrs, name=name)
        output = []
        # Normalize to strings
        str_values = set([force_text(v) for v in value])
        counter = 1
        for i in self.choices.queryset:
            cb = forms.CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
            option_value = force_text(i.id)
            rendered_cb = cb.render(name, option_value)
            option_label = conditional_escape(force_text(i.account_type))
            if counter % 2 == 0:
                output.append('<div class="span7"><label class="checkbox inline">%s %s</label>' % (rendered_cb, option_label))
                output.append('</div></div>')
            else:
                output.append('<div class="row-fluid"><div class="span5"><label class="checkbox inline">%s %s</label>' % (rendered_cb, option_label))
                output.append('</div>')
                if counter == len(self.choices.queryset):
                    output.append('</div>')

            counter += 1

        return mark_safe('\n'.join(output))
