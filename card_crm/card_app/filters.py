import django_filters
from django.forms.widgets import DateInput

from .models import Card


class CardFilter(django_filters.FilterSet):

    
    serial_number = django_filters.ChoiceFilter(choices=[], empty_label = 'Series')
    number = django_filters.ChoiceFilter(choices=[], empty_label = 'Number')
    status = django_filters.ChoiceFilter(choices=Card.choices, empty_label = 'Status')

    released_date = django_filters.DateFilter(field_name='released_date',
                                           widget= DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='contains', label='released_date')

    expired_date = django_filters.DateFilter(field_name='expired_date',
                                           widget= DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='contains', label='expired_date')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['serial_number'].extra['choices'] = [
            (serial_number, serial_number)
            for serial_number in Card.objects.values_list('serial_number', flat=True).distinct()
        ]
        self.filters['number'].extra['choices'] = [
            (number, number)
            for number in Card.objects.values_list('number', flat=True).distinct()
        ]

    class Meta:
        model =  Card
        fields = ['serial_number', 'number', 'released_date', 'expired_date', 'status', 'user']
