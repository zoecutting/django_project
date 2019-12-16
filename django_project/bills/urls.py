from django.urls import path
from . import views

urlpatterns = [
    path('', bills.home, name='bills-home'),
]
