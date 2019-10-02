from django import forms

from adhocracy4.categories import forms as category_forms

from . import models


class SpeakupIdeaForm(category_forms.CategorizableFieldMixin, forms.ModelForm):
    class Meta:
        model = models.SpeakupIdea
        fields = ['name', 'description', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.module.category_set.all():
            self.fields['category'].empty_label = '---'
        else:
            del self.fields['category']
