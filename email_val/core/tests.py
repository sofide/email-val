import pytest

from core.validation import save_email, random_validation, api_validation
from core.models import Email, Status


@pytest.mark.django_db
def test_save_email():
    email = 'prueba@bla.com'
    validation = random_validation(email)
    save_email(validation)
    assert Email.objects.filter(email=email).exists()


def test_api_validation(mocker):
    mocked_requests = mocker.patch('core.validation.requests', autospec=True)
    mocked_requests.get('url').json.return_value = 'JSON RESULT'
    result = api_validation('blabla')

    assert result == 'JSON RESULT'
