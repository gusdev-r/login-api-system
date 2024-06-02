from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UserRegistrationSerializer
from .utils import send_code_to_user


# Create your views here.
class RegistrationUserView(GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user_data = request.data
        user_serialized = self.serializer_class(data=user_data)
        if user_serialized.is_valid(raise_exception=True):
            user_serialized.save()
            user = user_serialized.data
            send_code_to_user(user['email'])

            print(user)
            return Response({
                'data': user,
                'message': 'hi! Thanks for signing up a passcode was sent to you email!'
            }, status=status.HTTP_201_CREATED)
        return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail