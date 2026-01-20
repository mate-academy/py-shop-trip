from decimal import Decimal
from app.customer import Customer
from app.shop import Shop


def calculate_products_cost(customer: Customer, shop: Shop) -> Decimal:
    return Decimal(str((customer.product_cart["milk"]
                        * shop.products["milk"]
                        + customer.product_cart["bread"]
                        * shop.products["bread"]
                        + customer.product_cart["butter"]
                        * shop.products["butter"])))
