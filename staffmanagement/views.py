from django.shortcuts import render
from usermanagement.serializers import *
from usermanagement.models import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        try:    
            user = User.objects.filter(is_staff=True)
            user_serializer = UsersSerializer(user, many=True)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_info(request,id):
    if request.method == 'GET':
        try:    
            info = User.objects.filter(id=id)
            user_serializer = UsersSerializer(info, many=True)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)            


@api_view(['GET'])
def transaction_list(request):
    if request.method == 'GET':
        try:    
            activity = Transactions.objects.all()
            transaction_serializer = TransactionSerializer(activity, many=True)
            return Response(transaction_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)