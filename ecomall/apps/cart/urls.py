from django.urls import path

from . import views

urlpatterns = [
    path('checkout/', views.paypal, name='checkout'),
    #path('payment/',views.payment,name='payment'),
    path('cart/', views.show_cart, name='cart'),
    path('success/', views.success, name='success'),

path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
path('online/lipa/payment/',views.Payment,name='payment'),

#register, confirmation, validation and callback urls
path('c2b/register', views.register_urls, name="register_mpesa_validation"),
path('c2b/confirmation', views.confirmation, name="confirmation"),
path('c2b/validation', views.validation, name="validation"),
path('c2b/callback', views.call_back, name="call_back"),
]

"""
"""