from django.db import models

from enums.transaction_status import TransactionStatus
from enums.transaction_type import TransactionType


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=TransactionType.choices,
    )
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=7,
        choices=TransactionStatus.choices,
    )

    account = models.ForeignKey(
        "account.Account",
        on_delete=models.PROTECT,
        related_name="transactions",
    )
    source_account = models.ForeignKey(
        "account.Account",
        on_delete=models.PROTECT,
        related_name="outgoing_transfers",
        null=True,
        blank=True,
    )
    destination_account = models.ForeignKey(
        "account.Account",
        on_delete=models.PROTECT,
        related_name="incoming_transfers",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "transaction"