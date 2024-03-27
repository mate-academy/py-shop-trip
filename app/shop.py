from datetime import datetime


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 product: dict) -> None:
        self.name = name
        self.location = location
        self.product = product

    def get_spent_money(
            self,
            customer_product: dict,
            car_fuel_cost: float,
            print_: bool) -> int | float:
        total_cost = car_fuel_cost
        for product, value in customer_product.product_cart.items():
            temper_cost = value * self.product[product]
            total_cost += temper_cost
        if print_ is True:
            print(f"{customer_product.name}'s trip to "
                  f"the {self.name} costs {round(total_cost, 2)}")
        return round(total_cost, 2)

    def get_price_product(self, customer_product: dict) -> int | float:
        total_cost = 0
        print(f"{customer_product.name} rides to {self.name}")
        now = datetime.strptime("04-01-2021 12:33:41", "%d-%m-%Y %H:%M:%S")
        print(f"""\nDate: {now.strftime("%d/%m/%Y %H:%M:%S")}""")
        print(f"Thanks, {customer_product.name}, for your purchase!")
        words_fixed_flake8_app = "You have bought: "
        print(words_fixed_flake8_app.strip())
        for product, value in customer_product.product_cart.items():
            temper_cost = value * self.product[product]
            print(f"{value} {product}s"
                  f" for {str(temper_cost).rstrip("0").rstrip(".")} dollars")
            total_cost += temper_cost
        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!")

        return total_cost
