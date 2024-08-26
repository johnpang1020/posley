from django.db import models
from django.utils import timezone

class Wallet(models.Model):
    address = models.CharField(max_length=255, unique=True)
    usdc_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    usdt_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    eth_balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.address

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE)
    currency = models.CharField(max_length=10)  # 'USDC', 'USDT', 'ETH'
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.address} - {self.currency} - {self.amount}"
