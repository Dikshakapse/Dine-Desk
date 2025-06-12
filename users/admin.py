from django.contrib import admin
from menu.models import DailyMenu
from orders.models import Order

admin.site.register(DailyMenu)
admin.site.register(Order)

