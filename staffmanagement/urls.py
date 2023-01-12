from django.urls import path
from . import views


urlpatterns = [
path('user_list/', views.user_list, name='user_list'),
path('user_info/<int:id>/', views.user_info, name='user_info'),
path('transaction_list/', views.transaction_list, name='transaction_list'),
]