from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=60, default='United States Dollar')
    short_name = models.CharField(max_length=10, default='USD')
    USD_price = models.FloatField(default=1)


class Wallet(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    available_money = models.FloatField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)


class Outlay(models.Model):
    amount = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    time = models.DateTimeField()
    name = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)


class Income(models.Model):
    amount = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    time = models.DateTimeField()
    source = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
