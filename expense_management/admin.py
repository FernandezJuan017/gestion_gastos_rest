from django.contrib import admin
from expense_management.models import (Category_Type,Category, Account,EffectType,TransactionType,
                                       LabelTransaction, Label, Transaction, Transfer)

# Register your models here.
admin.site.register(Category_Type)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(EffectType)
admin.site.register(TransactionType)
admin.site.register(Transaction)
admin.site.register(LabelTransaction)
admin.site.register(Label)
admin.site.register(Transfer)




