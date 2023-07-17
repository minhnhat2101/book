from django.shortcuts import render
from .models import Sach
# Create your views here.

def danh_sach(request):
    sach = Sach.objects.all()
    context = {
        'sach':sach
    }
    return render(request, "bookstore/index.html",context)



def timsach(request):        
    if request.method == 'GET': # this will be GET now      
        ten_sach =  request.GET.get('ten') # do some research what it does       
        status = Sach.objects.filter(tenSach__icontains=ten_sach) # filter returns a list so you might consider skip except part
        context = {
        'sach':status
         }
        return render(request, "bookstore/index.html",status)
    else:
        context = {
        'sach':""
         }
        return render(request,"search.html",{})