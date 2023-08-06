from django import forms
from common.models import File


class ImportFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'