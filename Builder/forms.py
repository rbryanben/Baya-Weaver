from django import forms
from .models import Theme


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('theme_name', 'template_file',)
