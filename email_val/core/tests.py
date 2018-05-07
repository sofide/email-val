import pytest

from core.validation import (save_email, random_validation, api_validation,
                             random_validation)
from core.models import Email, Status


EMAIL = 'prueba@bla.com'


@pytest.mark.django_db
def test_save_email():
    validation = random_validation(EMAIL)
    save_email(validation)
    assert Email.objects.filter(email=EMAIL).exists()


def test_api_validation(mocker):
    mocked_requests = mocker.patch('core.validation.requests', autospec=True)
    mocked_requests.get('url').json.return_value = 'JSON RESULT'
    result = api_validation(EMAIL)

    assert result == 'JSON RESULT'


def test_random_validation_result_keys():
    result = random_validation(EMAIL)

    for key in ['address', 'status', 'role_address']:
        assert key in result


def test_random_validation_result_email():
    result = random_validation(EMAIL)

    assert result['address'] == EMAIL
