from __future__ import annotations
import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int, int],
            products: dict[str, float],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_dict(
            cls,
            shop_dict: dict,
    ) -> Shop:
        return cls(
            shop_dict.get("name"),
            shop_dict.get("location"),
            shop_dict.get("products")
        )

    def service(self, customer_name: str, desired_products: dict) -> float:
        products_to_buy = {}
        total_cost = 0

        for product, quantity in desired_products.items():
            price = quantity * self.products[product]
            total_cost += price

            if float(price).is_integer():
                price = int(price)

            products_to_buy[product] = (quantity, round(price, 1))

        if float(total_cost).is_integer():
            total_cost = int(total_cost)

        print(
            Shop._write_receipt(
                customer_name,
                products_to_buy,
                total_cost
            )
        )
        return total_cost

    @staticmethod
    def _write_receipt(
            customer_name: str,
            bought_products: dict,
            total_cost: float | int,
    ) -> str:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = f"Date: {date}\n"
        receipt += f"Thanks, {customer_name}, for your purchase!\n"
        receipt += "You have bought:\n"
        for product, (quantity, price) in bought_products.items():
            receipt += f"{quantity} {product}s for {price} dollars\n"
        receipt += f"Total cost is {total_cost} dollars\n"
        receipt += "See you again!\n"
        return receipt
