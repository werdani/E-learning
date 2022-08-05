from django.urls import path
from . import views

urlpatterns = [
    path("",views.Assign_List),
    path("assignment_list/<int:id>/",views.Assignment_List),
]