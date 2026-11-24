from rest_framework import serializers

from .models import Transaction


class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
            "transaction_type",
            "transaction_date",
            "description",
            "status",
            "source_account",
            "destination_account",
        ]

from decimal import Decimal

from rest_framework import serializers

from enums.transaction_type import TransactionType


class TransactionRequestSerializer(serializers.Serializer):
    transaction_type = serializers.ChoiceField(choices=TransactionType.choices)
    amount = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        min_value=Decimal("0.01"),
    )
    account_number = serializers.CharField(max_length=15)
    destination_account_number = serializers.CharField(
        max_length=15,
        required=False,
    )
    description = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        if data["transaction_type"] == TransactionType.TRANSFER:
            if "destination_account_number" not in data:
                raise serializers.ValidationError({
                    "destination_account_number": "This field is required for transfers.",
                })

        return data