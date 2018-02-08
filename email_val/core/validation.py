import urllib
import json
import random

from collections import defaultdict


API_URL = 'https://bpi.briteverify.com/emails.json?'
API_KEY = None


def api_validation(email):
    url = API_URL + urllib.parse.urlencode({'adress': email, 'apikey': API_KEY})
    data = urllib.request.urlopen(url)
    data = data.read().decode()

    result = json.loads(data)

    return result


def random_validation(email):
    result = {
        'address': email,
        'status': random.choice(('valid', 'invalid', 'unknown', 'accept all'))
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
