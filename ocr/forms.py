# forms.py
from django import forms
from .models import ocrmodel

class OcrForm(forms.ModelForm):
    class Meta:
        model = ocrmodel
        fields = ('img',)

    def __init__(self, *args, **kwargs):
        super(OcrForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['style'] = "z-index: 999; opacity: 0; width: 320px; height: 200px; position: absolute; right: 0px; left: 0px; margin-right: auto; margin-left: auto;"
            self.fields[field].widget.attrs['multiple'] = 'multiple'
