import urllib
import json


API_URL = 'https://bpi.briteverify.com/emails.json?'
API_KEY = None


def validate(email):
    url = API_URL + urllib.parse.urlencode({'adress': email, 'apikey': API_KEY})
    data = urllib.request.urlopen(url)
    data = data.read().decode()

    result = json.loads(data)

    return result
