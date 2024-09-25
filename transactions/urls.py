from django.urls import path, include
from .views import *




urlpatterns = [
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:user_id>/transactions/', UserTransactionList.as_view(), name='user-transactions'),
    path('reports/', ReportView.as_view(), name='financial-report'),
]
