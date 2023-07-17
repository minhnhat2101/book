from django.shortcuts import render
from .models import Sach
# Create your views here.

def danh_sach(request):
    sach = Sach.objects.all()
    context = {
        'sach':sach
    }
    return render(request, "bookstore/index.html",context)