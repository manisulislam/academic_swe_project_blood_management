from django.shortcuts import render, redirect
from .models import Medicine, MedicineOrder
from django.contrib.auth.decorators import login_required

@login_required
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, "pharmacy/medicine_list.html", {"medicines": medicines})

@login_required
def order_medicine(request, med_id):
    if request.method == "POST":
        qty = int(request.POST.get("quantity"))
        MedicineOrder.objects.create(
            patient=request.user,
            medicine_id=med_id,
            quantity=qty
        )
        return redirect("my_orders")
    medicine = Medicine.objects.get(id=med_id)
    return render(request, "pharmacy/order_form.html", {"medicine": medicine})

@login_required
def my_orders(request):
    orders = MedicineOrder.objects.filter(patient=request.user)
    return render(request, "pharmacy/my_orders.html", {"orders": orders})
