from rest_framework import status
from django.shortcuts import render
from .serializers import UserSerializer, ForgotPasswordSerializer
from Rest_Auth_Test.user.models import User
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import generics
from rest_framework.views import APIView


# Create your views here.


class SignUp(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        print('request: ', request)
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


class get_post_users(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser,)

    # pagination_class = CustomPagination

    def get_queryset(self):
        users = User.objects.all()
        return users

    # Get all items
    def get(self, request):
        users = self.get_queryset()
        # paginate_queryset = self.paginate_queryset(items)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new item

    # def post(self, request):
    #     name = request.data.get('name')
    #     email = request.data.get('email')
    #     groups = request.data.get('groups')
    #     print('groups: ', groups)
    #     item = User.objects.


class UpdateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
