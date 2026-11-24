from django.db import models


class NotificationType(models.TextChoices):
    EMAIL = "EMAIL"
    SMS = "SMS"
    PUSH = "PUSH"