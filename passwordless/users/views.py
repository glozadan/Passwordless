from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from users.serializers import UserSignUpSerializer
from users.models import User



class UserSignUpView(APIView):

    permission_classes = [permissions.AllowAny]
    
    def post(self, request): 
        serializer = UserSignUpSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)
    

class UserSingleView(APIView):
    def get(self, request, id):
        user = User.objects.filter(id = id).first()
        if user is None:
            return Response({'error': 'Bad request'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = UserSignUpSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def patch(self, request, id):
        user = User.objects.filter(id = id).first()
        if user is None:
            return Response({'error': 'Bad request'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = UserSignUpSerializer(user, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK) 

    def delete(self, request, id):
        user = User.objects.get(id = id)
        user.delete()
        return Response({'msg': 'Cuenta exitosamente eliminada'}, status = status.HTTP_204_NO_CONTENT)
