from django import forms


class UploadCsvForm(forms.Form):
    csv = forms.FileField(label="")
    columns = forms.CharField(
        max_length=200,
        initial=2,
        label='Number of columns where emails are, separeted by comma'
    )
    delimiter = forms.CharField(
        max_length=1,
        initial=',',
        label='Field delimiter'
    )
    has_headers = forms.BooleanField(
        required=False,
        initial=True,
        label='The first row has columns headers'
    )
