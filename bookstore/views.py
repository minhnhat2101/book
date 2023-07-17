from django.shortcuts import render

# Create your views here.

def danh_sach(request):
    return render(request, "bookstore/index.html")