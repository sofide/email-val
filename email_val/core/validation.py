import random
import requests

from collections import defaultdict


API_URL = 'https://bpi.briteverify.com/emails.json'
API_KEY = None


def api_validation(email):
    data = requests.get(API_URL, params={'address': email, 'apikey': API_KEY})

    result = data.json()

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
        result = validation_function(email)
        validations[result['status']].append(email)

    return validations, validated_by
