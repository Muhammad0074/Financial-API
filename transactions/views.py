from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.response import Response
from django.utils.timezone import now


class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.query_params.get('user')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if user:
            queryset = queryset.filter(user__id=user)
        if start_date and end_date:
            queryset = queryset.filter(transaction_date__range=[start_date, end_date])
        
        return queryset


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserTransactionList(generics.ListAPIView):
    serializer_class = TransactionSerializer
    

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transaction.objects.filter(user__id=user_id)



class ReportView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date', now())

        transactions = Transaction.objects.filter(
            user__id=user_id,
            transaction_date__range=[start_date, end_date]
        )

        total_amount = transactions.aggregate(Sum('amount'))['amount__sum']
        data = {
            'total_transactions': transactions.count(),
            'total_amount': total_amount,
        }
        return Response(data)
