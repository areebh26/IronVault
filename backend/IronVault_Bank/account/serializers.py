from rest_framework import serializers

from transaction.serializers import TransactionDetailSerializer
from .models import Account


class AccountDetailSerializer(serializers.ModelSerializer):
    transactions = TransactionDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Account
        fields = [
            "id",
            "account_number",
            "account_type",
            "currency",
            "status",
            "closed_at",
            "created_at",
            "updated_at",
        ]