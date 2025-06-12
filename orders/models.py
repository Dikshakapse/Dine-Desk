from django.db import models

# Create your models here.
from menu.models import DailyMenu
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(DailyMenu, on_delete=models.CASCADE)
    order_type = models.CharField(choices=[('full', 'Full'), ('half1', 'Half Type 1'), ('half2', 'Half Type 2')], max_length=10)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
