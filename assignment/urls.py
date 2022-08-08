from django.urls import path
from . import views

urlpatterns = [
    path("",views.Assign_List),
]