from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from core.forms import UploadCsvForm, LoginForm
from core.validation import validator


def home(request):

    if request.method == 'POST':
        csv_form = UploadCsvForm(request.POST, request.FILES)

        if csv_form.is_valid():
            data = request.FILES['csv'].read().decode().split('\n')
            delimiter = csv_form.cleaned_data['delimiter']
            data = [line.split(delimiter) for line in data]

            if csv_form.cleaned_data['has_headers']:
                data = data[1:]

            columns = csv_form.cleaned_data['columns'].split(',')

            try:
                columns = [int(n) for n in columns]
            except ValueError:
                warnings = 'Invalid columns format. You have to put' \
                           'numbers separated by  commas. For example: 0, 3'

                return render(request, 'core/home.html', {'csv_form': csv_form,
                                                          'warning': warnings})
            emails = [line[col]
                      for line in data
                      for col in columns
                      if len(line) > col]

            emails_validations, validated_by = validator(emails)

            return render(request, 'core/home.html', {
                'csv_form': csv_form,
                'emails': emails,
                'emails_validations': emails_validations,
                'validated_by': validated_by,
            })

    else:
        csv_form = UploadCsvForm()

    return render(request, 'core/home.html', {'csv_form': csv_form})


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

        error_message = ('Invalid login. Please complete the form '
                         'with your username and password')
        return render(request, 'core/login.html', {
            'error_message': error_message,
            'login_form': login_form,
        })

    else:
        login_form = LoginForm()
        return render(request, 'core/login.html', {'login_form': login_form})
