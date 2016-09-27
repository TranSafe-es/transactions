from django.db import models
from objects.models import Object
import uuid


class Transactions(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    buyer_uuid = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True)
    seller_uuid = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True)
    object = models.ForeignKey(Object, blank=False)
    price = models.FloatField(blank=False)

    AWAITING_SELLER_CONFIRMATION = "Awaiting seller confirmation"
    AWAITING_PAYMENT = "Awaiting payment"
    AWAITING_SHIPPING = "Awaiting shipping"
    SHIPPED = "Shipped"
    REFUND = "Refund"
    COMPLETED = "Completed"

    STATE = (
        (AWAITING_SELLER_CONFIRMATION, "Awating seller confirmation"),
        (AWAITING_PAYMENT, "Awaiting payment"),
        (AWAITING_SHIPPING, "Awaiting shipping"),
        (SHIPPED, "Shipped"),
        (REFUND, "Refund"),
        (COMPLETED, "Completed"),
    )

    state = models.CharField(choices=STATE, db_index=True, default=AWAITING_SELLER_CONFIRMATION, max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
