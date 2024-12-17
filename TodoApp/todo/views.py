# from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializers,SignupSerializer
from rest_framework import viewsets,status
from .filters import TodoFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions,AllowAny,IsAuthenticated
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter
    #overiding global specified
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user) 
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)

class Auth(viewsets.ViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["post"],permission_classes=[AllowAny])
    def signup(self,req):
        serializer = SignupSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created"},status=status.HTTP_200_OK)
        return Response({"error":"invalid creds"},status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False,methods=["post"],permission_classes=[AllowAny])
    def login(self,req):
        username = req.data["username"]
        password = req.data["password"]
        user = authenticate(request=req,username = username,password = password)
        if user is not None:
            login(request=req,user=user)
            return Response({"msg":"login sucess"},status=status.HTTP_200_OK)
        return Response({"error":"invalid creds"},status=status.HTTP_401_UNAUTHORIZED)


    @action(detail=False,methods=["post"])
    def logout(self,req):
        logout(req)
        return Response({"msg":"logout sucess"},status=status.HTTP_200_OK)