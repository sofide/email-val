import random
import requests

from collections import defaultdict


API_URL = 'https://bpi.briteverify.com/emails.json'
API_KEY = None


def api_validation(email):
    data = requests(API_URL, params={'adress': email, 'apikey': API_KEY})

    result = data.json()

    if result['status'] == 'accept all':
        result['status'] = 'accept_all'

    return result


def random_validation(email):
    result = {
        'address': email,
        'status': random.choice(('valid', 'invalid', 'unknown', 'accept_all'))
    }

    return result


def validator(emails_list):
    if API_KEY:
        validation_function = api_validation
        validated_by = 'api'
    else:
        validation_function = random_validation
        validated_by = 'random'

    validations = defaultdict(list)

    for email in emails_list:
        result = validation_function
        validations[result['status']].append(email)

    return validations, validated_by
