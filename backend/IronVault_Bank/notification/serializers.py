from rest_framework import serializers

from .models import Notification


class NotificationDetailSerializer(serializers.ModelSerializer):
    template_name = serializers.CharField(required=False)
    template_variables = serializers.DictField(required=False)

    class Meta:
        model = Notification
        fields = [
            "id",
            "subject",
            "recipient",
            "body",
            "notification_type",
            "created_at",
            "template_name",
            "template_variables",
        ]