from rest_framework import serializers
from orders.models import Order
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email

        return token