from django.db import models

from enums.notification_type import NotificationType


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    recipient = models.EmailField()
    body = models.TextField()
    notification_type = models.CharField(
        max_length=5,
        choices=NotificationType.choices,
        default=NotificationType.EMAIL,
    )
    user = models.ForeignKey(
        "auth_user.User",
        on_delete=models.PROTECT,
        related_name="notifications",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notifications"