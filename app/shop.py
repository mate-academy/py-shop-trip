from app import utils


class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name: str = shop_info["name"]
        self.location: list[int] = shop_info["location"]
        self.products: dict = shop_info["products"]

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        print(f"Date: {utils.get_datetime()}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0.0
        for product, amount in product_cart.items():
            cost = utils.float_to_int(amount * self.products[product])
            print(f"{amount} {product}s for {cost} dollars")
            total_cost += cost

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
