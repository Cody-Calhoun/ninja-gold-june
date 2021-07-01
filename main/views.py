from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.


def home(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['result'] = []
    return render(request, 'home.html')


def process_money(request):
    building = request.POST['type']
    original_gold = request.session['gold']
    if building == "farm":
        request.session['gold'] += random.randint(10, 20)
    elif building == "cave":
        request.session['gold'] += random.randint(5, 10)
    elif building == "house":
        request.session['gold'] += random.randint(2, 5)
    else:
        request.session['gold'] += random.randint(-50, 50)

    transaction_time = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if request.session['gold'] < original_gold:
        gold_lost = abs(original_gold - request.session['gold'])
        message = f"Uh-Oh you lost {gold_lost} golds from the {building}! ({transaction_time})"
    else:
        message = f"Earned {abs(original_gold-request.session['gold'])} gold from the {building}! ({transaction_time})"
    request.session['result'].append(message)

    return redirect('/')
