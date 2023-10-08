from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.sessoin = request.session
        cart = self.sessoin.get(settings.CART_SESSION_ID)
        if not cart:
            #              сохраняем Пустую корзину в сессии
            cart = self.sessoin[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем еовары в карзине и получаем товары из базы данных.
        """
        product_ids = self.cart.keys()
        #       получаем товары и добовляем их в карзину
        product = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in product:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Считаем сколько товаров в карзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        #       сохраняем товар
        self.sessoin.modified = True

    def remove(self, product):
        """
        Удаляем товар
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        #       получаем общую стоймость

        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        #       очищаем карзину в сессии
        del self.sessoin[settings.CART_SESSION_ID]
        self.save()
