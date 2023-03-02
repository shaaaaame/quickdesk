from django.urls import path

from . import views

urlpatterns = [
    path('manager/', views.counter, name='counter'),
    path('customer/', views.customer, name='customer'),
    path('', views.index, name='index'),
]