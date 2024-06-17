import datetime

from app.customers import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cost_for_products(
            self,
            product_cart: dict
    ) -> float:
        total_sum = 0
        for product in product_cart:
            total_sum += product_cart[product] * self.products[product]

        return total_sum

    @staticmethod
    def format_price(price: float) -> int | float:
        return int(price) if price.is_integer() else float(price)

    def give_purchase_receipt(
            self,
            client: Customer
    ) -> None:
        print(f"\nDate: "
              f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
        print(f"Thanks, {client.name}, for your purchase!\nYou have bought:")
        for product in client.product_cart:
            current_product = (client.product_cart[product]
                               * self.products[product])
            print(f"{client.product_cart[product]} {product}s "
                  f"for "
                  f"{self.format_price(current_product)} "
                  f"dollars")
        print(f"Total cost is "
              f"{self.calculate_cost_for_products(client.product_cart)} "
              f"dollars\nSee you again!")
