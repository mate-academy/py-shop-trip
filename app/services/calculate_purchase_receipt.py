from app.models.customer.customer import Customer
from app.models.shop.shop import Shop
from app.models.purchase.purchase_receipt_generator import (
    PurchaseReceiptGenerator,
)
from app.models.purchase.purchase_receipt_item import PurchaseReceiptItem


def calculate_customer_purchase_receipt(
        customer: Customer,
        choosen_shop: Shop
) -> PurchaseReceiptGenerator:
    bought_products: list[PurchaseReceiptItem] = []
    total_cost = 0

    for product, quantity in customer.product_cart.items():
        product_price = choosen_shop.products.get(product, 0)

        if product_price is None:
            continue

        product_cost = quantity * product_price

        bought_products.append(
            PurchaseReceiptItem(
                product=product,
                quantity=quantity,
                product_cost=product_cost,
            )
        )

        total_cost += product_cost

    return PurchaseReceiptGenerator(
        bought_products=bought_products,
        total_cost=total_cost,
    )
