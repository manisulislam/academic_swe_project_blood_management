from django.shortcuts import render
from .models import Test, LabReport
from django.contrib.auth.decorators import login_required

@login_required
def test_list(request):
    tests = Test.objects.all()
    return render(request, "labs/test_list.html", {"tests": tests})

@login_required
def my_lab_reports(request):
    reports = LabReport.objects.filter(patient=request.user)
    return render(request, "labs/my_reports.html", {"reports": reports})
