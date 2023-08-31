import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: list[float],
        products: dict[str, float],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_total(
        self, product_cart: dict[str, int]
    ) -> tuple[float, str]:
        total: float = 0
        products_info: list[str] = []
        for product, quantity in product_cart.items():
            product_price: float = self.products[product] * quantity
            total += product_price
            products_info.append(
                f"{quantity} {product}s for {round(product_price, 2)} dollars"
            )
        return total, "\n".join(products_info)

    def purchase_products(
        self, customer: "Customer", product_cart: dict[str, int]
    ) -> str:
        total_price, products = self.calculate_total(product_cart)
        receipt: str = (
            f"\nDate: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: \n"
            f"{products}\n"
            f"Total cost is {total_price} dollars\n"
            f"See you again!\n"
        )
        customer.money -= total_price
        return receipt
