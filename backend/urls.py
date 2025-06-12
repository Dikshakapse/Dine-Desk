from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('About/', views.aboutpage, name='about'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('order/', views.order_view, name='order'),
]
