from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet, TiffinProviderViewSet, DailyMenuViewSet, OrderViewSet, BillingViewSet, FeedbackViewSet, DeliveryTrackingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'tiffin-providers', TiffinProviderViewSet)
router.register(r'daily-menus', DailyMenuViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'billings', BillingViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'delivery-tracking', DeliveryTrackingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]