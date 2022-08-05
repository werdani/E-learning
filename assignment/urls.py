from django.urls import path
from . import views

urlpatterns = [
    path("",views.Assign_List),
    path("assignment/<int:id>/",views.Assignment_List),
]