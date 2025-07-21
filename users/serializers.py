from rest_framework import serializers
from .models import User, UserProfile, TiffinProvider, DailyMenu, Order, Billing, Feedback, DeliveryTracking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_tiffin_provider']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'address', 'phone_number', 'purchase_history']

class TiffinProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiffinProvider
        fields = ['id', 'user', 'name', 'address', 'phone_number']

class DailyMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMenu
        fields = ['id', 'tiffin_provider', 'date', 'full_tiffin_items', 'half_tiffin_items']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'tiffin_provider', 'menu', 'order_type', 'quantity', 'status', 'created_at']

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['id', 'user', 'month', 'total_amount', 'paid']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'tiffin_provider', 'rating', 'comments', 'created_at']

class DeliveryTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTracking
        fields = ['id', 'order', 'current_location', 'estimated_delivery_time', 'status']
