from django.contrib import admin
from django.urls import path,include
from bookstore import views
urlpatterns = [
    path('',views.danh_sach, name="danh_sach"),
    path('/timsach',views.timsach, name="timsach"),
    path('<int:book_id>', views.update_book, name="update_book"),
    path('update_process/', views.update_process, name="update_process"),
]
