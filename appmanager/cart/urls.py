from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_about, name='cart_about'),
    path('add/<int:product_id>/', views.cart_add, name='card_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

]
