from django.urls import path
from shop import views
from .views import Login, logout_func, Register

app_name = 'shop'

urlpatterns = [

    path('', views.product_index, name='product_index'),
    path('<slug:category_slug>', views.product_index, name='product_index_by_category'),
    path('<int:id>/<slug:slug>/', views.product_about, name='product_about'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_func, name='logout'),
]
