from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views


urlpatterns = [
  
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('view_user/<int:id>/', views.view_user, name='view_user'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('send_money/', views.send_money, name='send_money'),
    path('request_money/', views.request_money, name='request_money'),
    path('activity/', views.activity, name='activity'),
]