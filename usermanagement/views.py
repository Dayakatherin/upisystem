from django.shortcuts import render
from usermanagement.serializers import *
from usermanagement.models import *
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import logout as auth_logout

from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def register(request): 
    if request.method == 'POST':
        user_serializer = RegisterSerializer(data=request.data)
        if user_serializer.is_valid():
            
            user = User.objects.create_user(user_serializer.data['username'], user_serializer.data['email'], user_serializer.data['password'])
            token = Token.objects.create(user=user)
            data = {"Token": token.key}
            return Response(data, status=status.HTTP_200_OK)
        data = {'Error':'User already exist!'}
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET']) 
def logout(request):
    auth_logout(request)
    data = {'Success': 'Sucessfully logged out'}
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_user(request,id):
    if request.method == 'GET':
        try:    
            user = User.objects.filter(id=id)
            user_serializer = UsersSerializer(user, many=True)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])   
def update_user(request,id):
   
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'Error': 'User does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'GET':
            user_serializer = UsersSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            user_data = request.data
            user_serializer = UsersSerializer(user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

            

@api_view(['POST'])   
def send_money(request):   
    if request.method == 'POST':
        try:
            transaction_data = request.data
            transaction_serializer = TransactionSerializer(data=transaction_data)
            if transaction_serializer.is_valid():
                transaction_serializer.save()
                return Response(transaction_serializer.data, status=status.HTTP_200_OK)
            return Response(transaction_serializer.errors, status=status.HTTP_403_FORBIDDEN)  
        except:
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET'])
def request_money(request, format=None):
    content = {'Pending payment request from KSEB'}
    return Response(content)            

@api_view(['GET'])
def activity(request):
    if request.method == 'GET':
        try:    
            activity = Transactions.objects.all()
            transaction_serializer = TransactionSerializer(activity, many=True)
            return Response(transaction_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)


