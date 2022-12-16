from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random

from .models import Card, Transaction
from .forms import GenerateCardForm
from .filters import CardFilter


def index(request):
    generate_card = GenerateCardForm
    if request.method == 'GET':
        transaсtions = Transaction.objects.all()
    if request.method == 'POST':
        if request.POST.get('card'):
            transaсtions = Transaction.objects.filter(card=request.POST.get('card'))
        else:
            transaсtions = Transaction.objects.all()
    users = User.objects.all()
    filter = CardFilter(request.GET, queryset=Card.objects.all())
    cards = filter.qs
    context = {
        'users': users,
        'cards': cards,
        'generate_card': generate_card,
        'filter': filter,
        'transaсtions': transaсtions,
    }
    return render(request, 'dashboard.html', context=context)


def transactions(request):
    return render(request, 'transactions.html')

def change_status(request, pk):
    card = Card.objects.get(pk=pk)
    if card.status == 'activated':
        card.status = 'deactivated'
        card.save()
    else:
        card.status = 'activated'
        card.save()
    return redirect('home')


def delete_card(request, pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return redirect('home')


def generate_card(request):
    if request.method == 'POST':
        serial_number = int(request.POST.get('serial_number'))
        amount = int(request.POST.get('amount'))
        user = User.objects.get(id=request.POST.get('user'))
        expired_date = request.POST.get('expired_date')
        for i in range(amount):
            number = random.randint(100000000000, 999999999999)
            card = Card(user=user, 
                        serial_number=serial_number, 
                        balance=1000, 
                        number=number,
                        expired_date=expired_date,
            )
            card.save()
        return redirect('home')