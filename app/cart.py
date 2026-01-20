from __future__ import annotations

from dataclasses import dataclass

from app.product import Product


@dataclass
class Cart:
    product_name: Product.name
    product_amount: int
