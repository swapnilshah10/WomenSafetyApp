from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

#for markers
@api_view(['GET'])
def getmarkers(request):
     if request.method == 'GET':
        try:
            user = request.user
            markers = Marker.get_all_markers(user)
            serializer = MarkersSerializer(markers, many=True)
            return Response(serializer.data)   
        except Marker.DoesNotExist : return Response(status = status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def postmarker(request):
        if request.method == 'POST':
            data = request.data  
            user = request.user   
            # data['user_id'] = user
            serializer = MarkersSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user_id = user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def deletemarker(request,id):
      if request.method == 'POST':
            try:
                Marker.objects.get(id=id).delete()
                return Response(status=status.HTTP_200_OK)
            except Marker.DoesNotExist:
              return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postlocation(request):
        if request.method == 'POST':
            data = request.data  
            # user = request.user   
            # data['user_id'] = user
            serializer = LocationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)