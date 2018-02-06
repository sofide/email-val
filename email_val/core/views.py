from django.shortcuts import render

from core.forms import UploadCsvForm


def home(request):
    if request.method == 'POST':
        csv_form = UploadCsvForm(request.POST)

        if csv_form.is_valid():
            return render(request, 'core/result.html')

    else:
        csv_form = UploadCsvForm()

    return render(request, 'core/home.html', {'csv_form': csv_form})
