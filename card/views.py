from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

# Create your views here.
def base(request):
    return render(request, 'card/main_list.html', {})

def record(request):
    return render(request, 'card/record.html', {})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = OrderForm()
    
    return render(request, 'card/add_order.html',)
    