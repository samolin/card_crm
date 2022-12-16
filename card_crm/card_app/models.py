from django.db import models
import random
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from django.core.validators import MaxValueValidator
from dateutil.relativedelta import relativedelta
import pytz


class Card(models.Model):
    
    choices = (
        ('activated', 'activated'),
        ('deactivated', 'deactivated'),
        ('expired', 'expired'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    serial_number = models.IntegerField(validators=[MaxValueValidator(9999)])
    number = models.IntegerField(
        default=random.randint(100000000000, 999999999999),
        primary_key=True,
        unique=True,
        validators=[MaxValueValidator(999999999999)]
    )
    released_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField(default = datetime.now() + relativedelta(years=+1))
    last_used = models.DateField(auto_now_add=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=1000.00)
    status = models.CharField(choices=choices, default='deactivated', max_length=11)


    @property
    def is_overdue(self):
        utc = pytz.UTC
        if self.expired_date.replace(tzinfo=utc) <= datetime.now().replace(tzinfo=utc):
            self.status = 'expired'
            self.save()
            return self.status
        else:
            return self.status

    @property
    def time_expired_date(self):
        datetime = self.expired_date.strftime("%d.%m.%Y %H:%M:%S")
        return datetime
    
    @property
    def time_released_date(self):
        datetime = self.released_date.strftime("%d.%m.%Y %H:%M:%S")
        return datetime
    
    def __str__(self):
        return f"{self.serial_number}-{self.number}"

    
class Transaction(models.Model):
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='transactions')
    purchase = models.CharField(max_length=255)

    @property
    def time_transaction(self):
        datetime = self.date.strftime("%d.%m.%Y %H:%M:%S")
        return datetime
    
    @classmethod
    def buy(cls, amount, card, purchase):
        if amount > card.balance:
            raise ValueError("You don't have enough money")
        card.balance -= amount
        card.save()
        return card, amount

    def __str__(self):
        return f'{self.amount}'

    

