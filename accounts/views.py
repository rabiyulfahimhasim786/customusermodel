from os import stat
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, response
from django.contrib.auth import get_user_model, login, logout, authenticate
from rest_framework import permissions, serializers
import rest_framework
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import profile
from .serializers import (
    GetUserserializer,
    User , 
    Userupdateserializer,
    Loginserializer,
    profileserializer,
    changepasswordserializer,
    signupserializer,
)

def home_screen_view(request):
    return render(request, 'accounts/home.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def account_view(request):
    return render(request, 'accounts/account.html')

def register_view(request):
    return render(request, 'accounts/register.html')


def index(request):
    return HttpResponse("Hello, world. You're at the accounts index.")
# Create your views here.

class signupapiview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = signupserializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = signupserializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status":"ok"},status=status.HTTP_200_OK,)
        return Response({"status":"failed to created a data"},status=status.HTTP_403_FORBIDDEN)


class Changepasswordapiview(CreateAPIView):
    serializer_class  = changepasswordserializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializers = changepasswordserializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status":"ok"},status = status.HTTP_201_CREATED)
        return Response({"status":"ok"},status = status.HTTP_401_UNAUTHORIZED)



class UserLoginApiview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Loginserializer


    def post(self, request):
        username  = request.data.get("phone",None)
        password = request.data.get("password",None)
        if username and password:
            user = authenticate(username = username , password = password)
            if user:
                login(request , user)
                token , created = Token.objects.get_or_create(user = user)
                data  = {
                    "id" : user.id,
                    "token" : token.key,
                    "username" : user.phone,
                    "is_admin" : user.is_admin,
                    "profile_id" : user.profile.id , 
                }

                return Response({"status":"ok created "},status=status.HTTP_201_CREATED)
            return Response({"status":"failed to create a data"},status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(
            {"status":"user should provide a valid credentials"}
        )


class LogoutApiview(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        logout(request)
        print("logout")
        return Response({"status":"ok"},status= status.HTTP_202_ACCEPTED)

class profileListapiview(ListAPIView):
    queryset = profile.objects.all()
    serializer_class = profileserializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        query = profile.objects.all()
        serializers = profileserializer(query , many=True)
        return Response({"status":"ok","data": serializers.data},status=status.HTTP_200_OK)


class UserListapiview(ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserserializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        query = User.objects.all()
        serializers = GetUserserializer(query , many=True)
        return Response({"status":"ok","data": serializers.data},status=status.HTTP_200_OK)



class ProfileUpdateApiview(RetrieveUpdateDestroyAPIView):
    queryset = profile.objects.all()
    serializer_class = profileserializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = profile.objects.all()
        prfile = get_object_or_404(queryset, pk=pk)
        serializer = profileserializer(prfile)
        return Response({"status": "success", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = profile.objects.all()
        prfile = get_object_or_404(queryset, pk=pk)
        serializer = profileserializer(prfile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "failure", "data": serializer.errors})


class UserUpdateApiview(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userupdateserializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        name = get_object_or_404(queryset , pk=pk)
        serializers = Userupdateserializer(name)
        return Response({"status": "success", "data": serializers.data})

    def update(self, request,pk=None):
        queryset = User.objects.all()
        name = get_object_or_404(queryset , pk=pk)
        serializers = Userupdateserializer(queryset , data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "success", "data": serializers.data})
        return Response({"status": "failure", "data": serializers.errors})
