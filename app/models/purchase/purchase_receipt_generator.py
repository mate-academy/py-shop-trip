import datetime
from dataclasses import dataclass, field

from app.models.purchase.purchase_receipt_item import PurchaseReceiptItem


@dataclass
class PurchaseReceiptGenerator:
    bought_products: list[PurchaseReceiptItem]
    total_cost: int | float
    purchase_date: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now()
    )
