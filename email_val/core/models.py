from django.db import models


class email(models.Model):
    VALID = 'va'
    INVALID = 'in'
    UNKNOWN = 'un'
    ACCEPT_all = 'aa'

    STATUS_CHOICES = (
        (VALID, 'Valid'),
        (INVALID, 'Invalid'),
        (UNKNOWN, 'Unknown'),
        (ACCEPT_all, 'Accept all'),
    )

    email = models.CharField(max_length=254, unique=True)
    last_validation = models.DateField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    error = models.CharField(max_length=200, blank=True)
    is_role_address = models.BooleanField(default=False)
