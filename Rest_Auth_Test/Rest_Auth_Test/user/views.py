from rest_framework import status
from django.shortcuts import render
from Rest_Auth_Test.user.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import UserSerializer, ForgotPasswordSerializer
# Create your views here.


class SignUp(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPassword(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_passrord = request.data.get('confirm_password')

        if email and password and confirm_passrord:
            try:
                user = User.objects.get(email=email)
                if password == confirm_passrord:
                    user.set_password(password)
                    user.save()
                    return Response({"msg": "Password created successfully"}, status=status.HTTP_201_CREATED)
                return Response({"msg": "Password and confirm password not match"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"msg": "Email does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "Something went wrong in input"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
