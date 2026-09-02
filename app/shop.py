import datetime


class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name: str = shop_info["name"]
        self.location: tuple = tuple(shop_info["location"])
        self.products_prices: dict = shop_info["products"]

    def get_summ_for_products(self, products_cart: dict) -> float:
        total_cost: float = 0
        for key in products_cart:
            total_cost += products_cart[key] * self.products_prices[key]
        return total_cost

    def print_recipe(self, customer: object) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for key, value in customer.product_cart.items():
            price = value * self.products_prices[key]
            print(f"{value} {key}s for {price:g} dollars")

        total = self.get_summ_for_products(customer.product_cart)
        print(f"Total cost is {total:g} dollars")
        print("See you again!\n")
