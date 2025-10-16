from .tokens import get_tokens_for_user
from utils.response.response import CustomResponse as cr 
from .serializers import (
    UserRegistrationSerailizer,
    UserLoginSerailizer,
    UserChangePasswordSerailizer,
)

from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from django.utils import timezone

from django.contrib.auth import authenticate


class UserRegistrationView(APIView):
    serializer_class=UserRegistrationSerailizer
    permission_classes=[AllowAny]

    def post(self,request):
        """
        Registering User Account
        """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return cr.success(
                message="Your account has been successfully registered",
                status=HTTP_201_CREATED
            )
        return cr.error(
            message="Form Validation Error",
            errors=serializer.errors
            )
    

class UserLoginView(APIView):
    serializer_class=UserLoginSerailizer
    permission_classes=[AllowAny]


    def post(self,request):
        """
        Logging User and generating tokens
        """
        serializer=self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return cr.error(
            message="Form Validation Error",
            errors=serializer.errors
            )

        email=serializer.data.get('email')
        password=serializer.validated_data.get('password')

        user=authenticate(email=email,password=password)
        if user is not None:
            token=get_tokens_for_user(user)
            user.last_login = timezone.now()
            return cr.success(
                data=token,
                message="You have been successfully logged in",
            )
        
        return cr.error(
            message="Invalid Credential provided",
            status=HTTP_401_UNAUTHORIZED
        )
    

class UserChangePasswordView(APIView):
        serializer_class=UserChangePasswordSerailizer
        permission_classes=[IsAuthenticated]

        def post(self,request):
            user=request.user
            serializer=self.serializer_class(
                data=request.data,
                context={'user':user}
            )
            if not serializer.is_valid():
                return cr.error(
                message="Form Validation Error",
                errors=serializer.errors
                )
            return cr.success(
                message="Your password has been successfully changed"
            )
