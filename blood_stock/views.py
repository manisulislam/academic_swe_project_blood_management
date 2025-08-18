from django.shortcuts import render, redirect
from .models import BloodStock
from .forms import StockForm
from django.contrib.auth.decorators import login_required

@login_required
def stock_view(request):
    stocks = BloodStock.objects.all()
    return render(request, 'blood_stock/stock_view.html', {'stocks': stocks})

@login_required
def update_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            bg = form.cleaned_data['blood_group']
            u = form.cleaned_data['units']
            obj, created = BloodStock.objects.get_or_create(blood_group=bg)
            obj.units += u
            obj.save()
            return redirect('view_stock')
    else:
        form = StockForm()
    return render(request, 'blood_stock/update_stock.html', {'form': form})
