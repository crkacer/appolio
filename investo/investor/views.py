from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from investo.models import InvestorAccount, InvestorAccountTransaction
from investo.core.account import Account as CoreAccount


class AccountDetailView(APIView):

    def put(self, request):
        pass

    def delete(self, request):
        pass


class AccountView(APIView):

    def get(self):
        pass

    def post(self, request):
        id = request.data.get("id")
        account = InvestorAccount.objects.filter(account_id=id).first()

        if account:
            account_deposits = InvestorAccountTransaction.objects.filter(account=account, transaction_type="Investor_Deposit").all()
            account_withdraws = InvestorAccountTransaction.objects.filter(account=account, transaction_type="Investor_Withdraw").all()
            core_account = CoreAccount(
                compound=True,
                report_interval="quarterly",
                interest_rate=0.09,
                deposits=account_deposits,
                withdraws=account_withdraws
            )

            returns_data = core_account.returns_data()
            chart_data = core_account.chart_data()
            report_data = core_account.report_data()
            body_data = {
                "returns": returns_data,
                "chart_data": chart_data,
                "report_data": report_data
            }
            return Response(data=body_data, status=status.HTTP_200_OK)
        return Response(data="Account Not Found", status=status.HTTP_400_BAD_REQUEST)