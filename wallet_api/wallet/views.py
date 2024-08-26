from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Wallet, Transaction
from .serializers import WalletSerializer

class WalletBalanceView(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletTransferVolumeView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        wallet_id = self.kwargs.get('pk')
        wallet = Wallet.objects.get(id=wallet_id)

        end_time = timezone.now()
        start_time = end_time - timedelta(hours=24)

        transactions = Transaction.objects.filter(
            wallet=wallet,
            timestamp__range=(start_time, end_time)
        )

        volumes = {
            'USDC': transactions.filter(currency='USDC').aggregate(total=models.Sum('amount'))['total'] or 0,
            'USDT': transactions.filter(currency='USDT').aggregate(total=models.Sum('amount'))['total'] or 0,
            'ETH': transactions.filter(currency='ETH').aggregate(total=models.Sum('amount'))['total'] or 0,
        }

        return Response(volumes)
