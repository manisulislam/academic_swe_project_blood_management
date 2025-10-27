from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Staff
from .forms import StaffForm  # We’ll create this form next
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Decorator for CBV
def staff_required(view_func):
    return login_required(view_func)  # Customize later if you want role-based access

# List view
@method_decorator(login_required, name='dispatch')
class StaffListView(View):
    def get(self, request):
        staff_members = Staff.objects.all().order_by('department', 'user__username')
        return render(request, 'hospital/staff_list.html', {'staff_members': staff_members})

# Detail view
@method_decorator(login_required, name='dispatch')
class StaffDetailView(View):
    def get(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        return render(request, 'hospital/staff_detail.html', {'staff_member': staff_member})

# Create view
@method_decorator(login_required, name='dispatch')
class StaffCreateView(View):
    def get(self, request):
        form = StaffForm()
        return render(request, 'hospital/staff_form.html', {'form': form})

    def post(self, request):
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
        return render(request, 'hospital/staff_form.html', {'form': form})

# Update view
@method_decorator(login_required, name='dispatch')
class StaffUpdateView(View):
    def get(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        form = StaffForm(instance=staff_member)
        return render(request, 'hospital/staff_form.html', {'form': form})

    def post(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        form = StaffForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
        return render(request, 'hospital/staff_form.html', {'form': form})

# Delete view
@method_decorator(login_required, name='dispatch')
class StaffDeleteView(View):
    def get(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        return render(request, 'hospital/staff_confirm_delete.html', {'staff_member': staff_member})

    def post(self, request, pk):
        staff_member = get_object_or_404(Staff, pk=pk)
        staff_member.delete()
        return redirect('staff_list')
