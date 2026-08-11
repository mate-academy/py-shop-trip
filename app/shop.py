import datetime


class Shop:
    def __init__(self, shop_data: dict) -> None:
        self.name = shop_data["name"]
        self.location = shop_data["location"]
        self.products = shop_data["products"]

    def calculate_product_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product_name, amount in product_cart.items():
            total_cost += self.products[product_name] * amount

        return total_cost

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict,
            total_cost: float,
    ) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product_name, amount in product_cart.items():
            item_cost = amount * self.products[product_name]
            if item_cost.is_integer():
                item_cost = int(item_cost)
            print(f"{amount} {product_name}s for {item_cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
