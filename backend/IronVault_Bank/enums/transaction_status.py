from django.db import models


class TransactionStatus(models.TextChoices):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PENDING = "PENDING"