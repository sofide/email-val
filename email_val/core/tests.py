import pytest

from core.validation import save_email, random_validation
from core.models import Email, Status


@pytest.mark.django_db
def test_save_email():
    email = 'prueba@bla.com'
    validation = random_validation(email)
    save_email(validation)
    assert Email.objects.filter(email=email).exists()
