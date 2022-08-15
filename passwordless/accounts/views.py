from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import AccountsSerializers
from accounts.models import Account


class AccountsView(APIView):

    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountsSerializers(accounts, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountsSerializers(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response (serializer.data, status = status.HTTP_201_CREATED)

class AccountsSingleView(APIView):
    def get(self, request, id):
        account = Account.objects.filter(id = id).first()
        if account is None:
            return Response({'error': 'Bad request'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = AccountsSerializers(account)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def patch(self, request, id):
        account = Account.objects.filter(id = id).first()
        if account is None:
            return Response({'error': 'Bad request'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = AccountsSerializers(account, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK) 
    
    def delete(self, request, id):
        account = Account.objects.get(id = id)
        account.delete()
        return Response({'msg': 'Cuenta exitosamente eliminada'}, status = status.HTTP_204_NO_CONTENT)

