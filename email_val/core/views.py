from django.shortcuts import render

from core.forms import UploadCsvForm


def home(request):
    csv_form = UploadCsvForm()

    if request.method == 'POST':

        data = request.FILES['csv'].read()
        if type(data) == bytes:
            data = data.decode()

        data = [mail.strip() for mail in data.split(';')]

        return render(request, 'core/home.html', {'csv_form': csv_form,
                                                  'emails': data})

    return render(request, 'core/home.html', {'csv_form': csv_form})
