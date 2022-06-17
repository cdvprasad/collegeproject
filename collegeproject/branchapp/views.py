from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *


# Create your views here.

def new(request):
    data = StudentInfo.objects.all()
    return render(request, 'branchapp/first.html', {'data': data})


def index(request):
    if request.method == "POST":
        StudentInfo.objects.create(
            student=request.POST['student'],
            department=request.POST['department'],
            nationality=request.POST['nationality'],
            phone_no=request.POST['phone_no'],
        )
        return HttpResponseRedirect(reverse('branchapp:ss'))
    return render(request, 'branchapp/second.html')


def detail(request, StudentInfo_id):
    data = get_object_or_404(StudentInfo_id, pk=StudentInfo_id)
    return render(request, 'branchapp/third.html', {'data': data})


def final(request):
    new_data = StudentInfo.objects.all()
    return render(request, 'branchapp/fourth.html', {'new_data': new_data})
