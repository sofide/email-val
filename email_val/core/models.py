from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Email(models.Model):
    email = models.CharField(max_length=254, unique=True)
    last_validation = models.DateField(auto_now=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name='emails'
        )
    error = models.CharField(max_length=200, blank=True)
    is_role_address = models.BooleanField(default=False)

    def __str__(self):
        return self.email
