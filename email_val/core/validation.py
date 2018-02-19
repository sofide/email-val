import random
import requests

from collections import defaultdict

from core.models import Email, Status


API_URL = 'https://bpi.briteverify.com/emails.json'
API_KEY = None


def api_validation(email):
    '''
    Connect with the API to validate emails and returns the json from response
    '''
    data = requests.get(API_URL, params={'address': email, 'apikey': API_KEY})

    result = data.json()

    return result


def random_validation(email):
    '''
    Returns a random validation
    '''
    result = {
        'address': email,
        'status': random.choice(('valid', 'invalid', 'unknown', 'accept_all')),
        'role_address': False,
    }

    return result


def save_email(api_validation):
    '''
    Save api response to database
    '''
    address = api_validation['address']
    status_label = api_validation['status']

    if not Status.objects.filter(status=status_label).exists():
        Status.objects.create(status=status_label)
    status = Status.objects.filter(status=status_label).first()

    if Email.objects.filter(email=address).exists():
        email = Email.objects.filter(email=address).first()
    else:
        email = Email(email=address)

    email.status = status
    email.is_role_address = api_validation['role_address']
    if 'error' in api_validation:
        email.error = api_validation['error']

    email.save()


def validator(emails_list):
    '''
    Validate all the emails in the given list, and save them in the database
    '''
    # if there is an api_key defined it use the API to validate, otherwise it
    # use a random validation
    if API_KEY:
        validation_function = api_validation
        validated_by = 'api'
    else:
        validation_function = random_validation
        validated_by = 'random'

    validations = defaultdict(list)

    for email in emails_list:
        result = validation_function(email)
        validations[result['status']].append(email)

    return validations, validated_by
