from rest_framework.views import APIView
from rentoro.models import RentalPropertyTransaction, RentalPropertyTransactionType
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def get_transaction_detail(request):
    try:
        data = request.data
        id = data.get('id')
        transaction = RentalPropertyTransaction.objects.filter(transaction_id=id).first()
        if transaction:
            return Response(transaction, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_all_unit_transactions(request):
    try:
        data = request.data
        unit_id = data.get('unit_id')
        all_trans = RentalPropertyTransaction.objects.filter(property_unit=unit_id).all()
        data = list(all_trans.value())
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class TransactionView(APIView):

    def get(self):
        pass
    def post(self):
        pass


class TransactionTypeView(APIView):

    def get(self):
        try:
            all_transaction_types = RentalPropertyTransactionType.objects.all().values()
            data = list(all_transaction_types)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            transaction_name = data.get("transaction_name")
            transaction_type = data.get("transaction_type")
            transaction_slug = data.get("transaction_slug")
            new_transaction = RentalPropertyTransactionType(
                transaction_name=transaction_name,
                transaction_type=transaction_type,
                transaction_slug=transaction_slug
            )
            new_transaction.save()

            return Response(new_transaction, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class UnitView(APIView):

    def post(self):
        pass
