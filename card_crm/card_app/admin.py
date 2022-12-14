from django.contrib import admin

from .models import Card, Transaction
from .forms import TransactionForm


@admin.register(Card)
class Card(admin.ModelAdmin):
    list_display = ['user', 
                   'serial_number', 
                   'number',
                   'expired_date',
                   'balance',
                   'status',
    ]
    list_filter = ['released_date']


@admin.register(Transaction)
class Card(admin.ModelAdmin):
    form = TransactionForm
    list_fields = '__all__' 

    
            

