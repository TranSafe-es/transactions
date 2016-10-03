from django.db import models
from objects.models import Object
import uuid


class Transactions(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    to_uuid = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True)
    from_uuid = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True)
    object = models.ForeignKey(Object, blank=False)
    price = models.FloatField(blank=False)

    AWAITING_CONFIRMATION = "Awaiting confirmation"
    AWAITING_PAYMENT = "Awaiting payment"
    AWAITING_SHIPPING = "Awaiting shipping"
    SHIPPED = "Shipped"
    REFUND = "Refund"
    COMPLETED = "Completed"

    STATE = (
        ("AWAITING_CONFIRMATION", AWAITING_CONFIRMATION),
        ("AWAITING_PAYMENT", AWAITING_PAYMENT),
        ("AWAITING_SHIPPING", AWAITING_SHIPPING),
        ("SHIPPED", SHIPPED),
        ("REFUND", REFUND),
        ("COMPLETED", COMPLETED),
    )

    state = models.CharField(choices=STATE, db_index=True, default=AWAITING_CONFIRMATION, max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
