from django.contrib import admin

from .models import Currency, Income, Outlay, Wallet


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    fields = ('name', 'short_name', 'USD_price', )
    list_display = ('name', 'USD_price', )
    search_fields = ('name', )


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    fields = ('user', 'available_money', 'currency', )
    list_filter = ('user', 'currency',)
    list_display = ('id', 'user', )
    search_fields = ('user', )


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    fields = ('amount', 'time', 'source', 'comment')
    search_fields = ('source', )