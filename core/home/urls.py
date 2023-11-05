from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home ),
    path("create/",views.create ),
    # path("update/<id>/",views.update_student),
    # path("delete/<id>/",views.delete_student),
    
]