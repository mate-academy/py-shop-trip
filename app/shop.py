import datetime


class Shop:
    def __init__(
            self,
            name: str,
            product_prices_list: dict[str: int],
            coordinates: list[int]
    ) -> None:

        if not Shop.check_if_prices_correct(product_prices_list):
            raise ValueError("Price can't be negative")
        self.name = name
        self.product_prices_list = product_prices_list
        self.coordinates = coordinates

    def calculate_one_product_cost(
            self,
            product: str,
            amount: int
    ) -> float | int | Exception:

        if product not in self.product_prices_list:
            raise KeyError("No such a product in the market")
        return self.product_prices_list[product] * amount

    def calculate_cart_cost(
            self,
            product_cart: dict[str: int]
    ) -> int | float:

        return sum(
            self.calculate_one_product_cost(product, amount)
            for product, amount in product_cart.items()
        )

    def purchase_receipt(
            self,
            customer_name: str,
            customer_product_cart: dict[str: int]
    ) -> None:

        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought:"
        )

        for product, amount in customer_product_cart.items():
            price = round(self.calculate_one_product_cost(product, amount), 2)
            string = f"{amount} {product}s for "
            if int(price) == price:
                string += f"{int(price)} "
            else:
                string += f"{price} "
            string += "dollars"
            print(string)

        print(f"Total cost is "
              f"{round(self.calculate_cart_cost(customer_product_cart), 2)}"
              f" dollars\nSee you again!"
              )

    @staticmethod
    def check_if_prices_correct(prices: dict[str: int]) -> bool:
        if any(price < 0 for price in prices.values()):
            return False
        return True
