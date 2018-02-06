from django import forms


class UploadCsvForm(forms.Form):
    csv = forms.FileField()

