from django.db import models


class AccountType(models.TextChoices):
    SAVINGS = "SAVINGS"
    CURRENT = "CURRENT"