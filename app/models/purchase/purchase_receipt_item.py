from dataclasses import dataclass


@dataclass
class PurchaseReceiptItem:
    product: str
    quantity: int | float
    product_cost: int | float
