from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# from django_enum_choices.fields import Enum
# from django_enum_choices.fields import EnumChoiceField

   
# Users
class User(AbstractUser):  
    @property
    def fullname(self) -> str:
        return f"{self.surmame}, {self.name}"
    
#CategyTypes        
class Category_Type(models.Model):
    name = models.CharField(max_length=50)
        
    def __str__(self) -> str:
        return self.name 
    
#Categories
class Category(models.Model):
    
    # class TypeCategory(Enum):
    #     INGRESOS = "INGRESO"
    #     GASTOS = "GASTO"
        
    class Meta:
        verbose_name_plural = 'Categories'
                
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, 
                                        related_name='child_categories', 
                                        null= True, blank= True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank= True)
    type = models.ForeignKey(Category_Type, on_delete=models.CASCADE, related_name='categories') #EnumChoiceField(TypeCategory, default=TypeCategory.INGRESOS)
               
    def __str__(self) -> str:
        return self.name
        
#Accounts
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "%s - %s" % (self.name, self.user.fullname)
    
#EffectTypes
class EffectType(models.Model):
    name = models.CharField(max_length=50)
        
    def __str__(self) -> str:
        return self.name 

#Transaction_Types
class TransactionType(models.Model):
    
    # class TypeEffect(Enum):
    #     INGRESO = "INGRESO"
    #     EGRESO = "EGRESO"
        
    type = models.CharField(max_length=100)
    effect = models.ForeignKey(EffectType,on_delete=models.CASCADE) #EnumChoiceField(TypeEffect, default=TypeEffect.INGRESO)
    
    def __str__(self) -> str:
        return "%s - Efecto: %s" % (self.type, self.effect.name)
    
 #LabelTransaction
class LabelTransaction(models.Model):
    label = models.ForeignKey('Label', on_delete=models.CASCADE)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
       
#Labels
class Label(models.Model):
    name = models.CharField(max_length=100)
    transactions = models.ManyToManyField('Transaction', related_name='trasaction_labels', through='LabelTransaction')
    
        
#Transactions
class Transaction(models.Model):
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True ,related_name='incomes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='incomes')
    account_transfer = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now())
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=100)
    labels = models.ManyToManyField('Label', related_name='labels_transactions', through='LabelTransaction')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"[{self.user.name}] {self.type.type} {self.date} ${self.amount} - {self.category.name}"
    
#Transfers
class Transfer(models.Model):
    origin_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='transfer_origin_transaction') 
    destination_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='transfer_destination_transaction') 
    date = models.DateTimeField(default=datetime.now())
    amount = models.DecimalField(max_digits=10, decimal_places=2)

