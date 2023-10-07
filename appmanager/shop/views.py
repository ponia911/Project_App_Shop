from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View
from shop.models import Category, Product
from cart.forms import CartAddProductForm
from django.template import RequestContext



def product_index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    return render(request, 'shop/product/index.html', {'category': category,
                                                           'categories': categories,
                                                           'products': products})

#def product_index(request, category_slug=None):
#    category = None
#    categories = Category.objects.all()
#    products = Product.objects.filter(available=True)
#    if category_slug:
#        category = get_object_or_404(Category, slug=category_slug)
#        products = products.filter(category=category)
#    else:
#        return render(request, 'shop/product/index.html', {'category': category,
#                                                           'categories': categories,
#                                                           'products': products})

def product_about(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/about.html', {'product': product,
                                                                            'cart_product_form': cart_product_form})



class Login(View):
    def get(self, request):
        context = {'form': AuthenticationForm()}
        return render(request, 'shop/product/login.html', context)

    def post(self, request):
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            login(request, form_login.get_user())
        return redirect('shop:product_index')

def logout_func(request):
    logout(request)
    return redirect('shop:product_index')

class Register(View):
    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, 'shop/product/register.html', context)

    def post(self, request):
        rf = UserCreationForm(data=request.POST)
        if rf.is_valid():
            rf.save()
            return redirect('shop:login')
            messages.error(request, rf.errors)
        return redirect('shop:register')

#def index(request):
#    return render(request, 'shop/index.html')


#def about(request):
#    return render(request, 'shop/about.html')





#def categories(request, about_id):
#    return HttpResponse(f'<h1>Про нас </h1<p>id: {about_id}</p>')


#def categories_by_slug(request, about_slug):
#    return HttpResponse(f'<h1>Про нас </h1<p>slug: {about_slug}</p>')


#def archive(request, year):
#    if year > 2000:
#        uri = reverse('about', args='sport', )
#        return redirect(uri)
#    return HttpResponse(f'<h1>Про нас </h1<p>{year}</p>')

