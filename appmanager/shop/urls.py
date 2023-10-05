from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

from .import converters

app_name = 'shop'
#register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [

    path('', views.product_index, name='product_index'),
    #path('about/', views.product_about, name='product_about'),
    path('<slug:category_slug>', views.product_index, name='product_index_by_category'),
    path('<int:id>/<slug:slug>/',  views.product_about, name='product_about'),
    path('login/', LoginView.as_view(), name='login'),
#    path('register/', RegisterUser.as_view, name='register'),
    #path('about/<slug:about_slug>/', views.categories_by_slug, name='about'),
    #path('archive/<year4:year>/', views.archive, name='archive')
]
