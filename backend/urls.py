from django.contrib import admin
from django.urls import path
from users import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('About/', views.aboutpage, name='about'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('order_view/', views.order_view, name='order'),
    path('customerview/', views.customerview, name='customerview'),
    path('order_list/', views.order_list, name='order_list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
