from django.db import models
from decimal import Decimal
from enums.account_status import AccountStatus
from enums.account_type import AccountType

# Create your models here.





class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_number = models.CharField(max_length=15, unique=True)
    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal("0.00"),
    )
    account_type = models.CharField(max_length=7, choices=AccountType.choices)
    user = models.ForeignKey(
        "auth_user.User",
        on_delete=models.PROTECT,
        related_name="accounts",
    )
    currency = models.CharField(max_length=3, default="PKR", editable=False)
    status = models.CharField(max_length=9, choices=AccountStatus.choices)

    closed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "accounts"