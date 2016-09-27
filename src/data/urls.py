from django.conf.urls import url
from .views import TransactionDetails, TransactionHistory, CreateTransaction, UpdateTransactionState

urlpatterns = [
               url(r'^details/(?P<transaction_id>.+)/$', TransactionDetails.as_view(), name="Show details"),
               url(r'^history/(?P<user_uuid>.+)/$', TransactionHistory.as_view(), name="Transactions history"),
               url(r'^new/$', CreateTransaction.as_view(), name="Create transaction"),
               url(r'^state/$', UpdateTransactionState.as_view(), name="Update transaction state"),
]
