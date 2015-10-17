from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(help_text='max. 42 megabytes')
