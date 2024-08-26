from django.urls import path
from .views import WalletBalanceView, WalletTransferVolumeView

urlpatterns = [
    path('wallet/<int:pk>/balance/', WalletBalanceView.as_view(), name='wallet-balance'),
    path('wallet/<int:pk>/transfer-volume/', WalletTransferVolumeView.as_view(), name='wallet-transfer-volume'),
]
