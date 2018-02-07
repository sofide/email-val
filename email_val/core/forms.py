from django import forms


class UploadCsvForm(forms.Form):
    csv = forms.FileField(label="")
    columns = forms.CharField(max_length=200,
                              label='Number of columns where emails are, separeted by comma')

