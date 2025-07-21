from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_tiffin_provider = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    purchase_history = models.JSONField(default=list)

    def __str__(self):
        return self.user.username

class TiffinProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tiffin_provider")
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class DailyMenu(models.Model):
    tiffin_provider = models.ForeignKey(TiffinProvider, on_delete=models.CASCADE, related_name="menus")
    date = models.DateField()
    full_tiffin_items = models.JSONField(default=list)
    half_tiffin_items = models.JSONField(default=list)
    def __str__(self):
        return f"Menu for {self.date} by {self.tiffin_provider.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    tiffin_provider = models.ForeignKey(TiffinProvider, on_delete=models.CASCADE, related_name="orders")
    menu = models.ForeignKey(DailyMenu, on_delete=models.CASCADE, related_name="orders")
    order_type = models.CharField(max_length=10, choices=[("full", "Full"), ("half", "Half")])
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="billings")
    month = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return f"Billing for {self.month} - {self.user.username}"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    tiffin_provider = models.ForeignKey(TiffinProvider, on_delete=models.CASCADE, related_name="feedbacks")
    rating = models.PositiveIntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Feedback by {self.user.username} for {self.tiffin_provider.name}"

class DeliveryTracking(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="tracking")
    current_location = models.CharField(max_length=255)
    estimated_delivery_time = models.DateTimeField()
    status = models.CharField(max_length=20, default="In Transit")
    def __str__(self):
        return f"Tracking for Order {self.order.id}"