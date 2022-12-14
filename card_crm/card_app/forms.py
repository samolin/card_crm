from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import Transaction


class GenerateCardForm(forms.Form):
    choices = (
        (datetime.now() + relativedelta(years=+1), 'year'),
        (datetime.now() + relativedelta(months=+6), '6 months'),
        (datetime.now() + relativedelta(months=+1), '1 month'),
    )

    serial_number = forms.IntegerField(
        min_value=1000,
        max_value=9999,
        widget=forms.NumberInput(attrs={"class":"myfield"})
    )
    amount = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={"class":"myfield"})
    )
    user = forms.ModelChoiceField(queryset=User.objects.all())
    expired_date = forms.ChoiceField(choices=choices)
 

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'

    def clean(self):
        try:
            Transaction.buy(**self.cleaned_data)
            return self.cleaned_data
        except:
            raise forms.ValidationError('Not enough money')

