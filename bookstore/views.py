from django.shortcuts import render, get_object_or_404
from .models import Sach
# Create your views here.

def danh_sach(request):
    sach = Sach.objects.all()
    context = {
        'sach':sach
    }
    return render(request, "bookstore/index.html",context)



def timsach(request):        
    if request.method == 'POST': # this will be GET now      
        ten_sach =  request.POST.get('ten') # do some research what it does       
        sach = Sach.objects.filter(tenSach__icontains=ten_sach) # filter returns a list so you might consider skip except part
        context = {
            'sach':sach
         }
        return render(request, "bookstore/index.html",context)
    else:
        context = {
        'sach':""
         }
        return render(request,"bookstore/index.html",context)
    
def update_book(request,book_id):
    book = get_object_or_404(Sach, id=book_id)
    context = {'book':book}
    return render(request,'bookstore/update.html',context)

def update_process(request):
    if request.method == 'POST':
        id = request.POST.get('book_id')
        tenSach = request.POST.get('tenSach')
        gia = request.POST.get('gia')
        tacGia = request.POST.get('tacGia')
        Sach.objects.filter(id=id).update(tenSach= tenSach,gia= gia, tacGia= tacGia)
        sach = Sach.objects.all()
        context = {'sach': sach}
    return render(request,"bookstore/index.html",context)
