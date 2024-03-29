from decimal import Decimal
from django.conf import settings
from app_shop.models import Product

class Cart:

    """ Initiation cart """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, update_quantity=False):
        """ Add product into cart """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = { 'quantity': 0,
            'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Update cart's session """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def remove(self, product):
        """ Delete product from cart """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """ Iteration into cart """
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        
        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['total_price'] = int(item['price']) * int((item['quantity']))
            yield item
    
    def __len__(self):
        """ Count products into cart"""
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(int(item['price']*item['quantity']) for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def get_total_quantity(self):
        total = 0
        for i in self.cart.values():
            total += i['quantity']
        return total
    
