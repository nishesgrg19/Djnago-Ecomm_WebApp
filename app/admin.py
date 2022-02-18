import imp
from django.contrib import admin
from app.models import Customer
from app.models import Product,Cart,OrderPlace
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderPlace)