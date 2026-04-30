

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import verify_password
from django.core.serializers import serialize
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import  Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from user_module.models import User
from user_module.serializer import UserSerializer, LoginUserSerializer, PasswordUpdateSerializer


# Create your views here.
class RegisterUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class =PageNumberPagination
    filter_backends =[]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LoginUser(ListCreateAPIView):
    serializer_class = LoginUserSerializer
    queryset = User.objects.all()
    pagination_class =PageNumberPagination

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginUserSerializer(data=data)
        serializer.is_valid()

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        try:
            user = User.objects.filter(email=email).first()
        except User.DoesNotExist:
            return Response ({"massage":"Invalid User"},status=HTTP_400_BAD_REQUEST)


        if not user.check_password(password):
            print("password incorrect")
            return Response ({"massage":"Invalid Password"},status=HTTP_400_BAD_REQUEST)

        return Response({"type":True , "user":user.email},status=HTTP_200_OK)

class PasswordUpdate(RetrieveUpdateAPIView):
    serializer_class = PasswordUpdateSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = PasswordUpdateSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password updated successfully"}, status=200)


