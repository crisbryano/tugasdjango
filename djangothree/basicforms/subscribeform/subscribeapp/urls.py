from django.urls import path
from subscribeapp import views


urlpatterns = [
    path('',views.customers, name='customers')
]