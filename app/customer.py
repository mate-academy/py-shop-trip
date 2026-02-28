import datetime


from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car_fuel_consumption: float) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car_fuel_consumption = car_fuel_consumption

    def make_purchase(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        print(f"""Date: {datetime.datetime.now()
              .strftime("%d/%m/%Y %H:%M:%S")}\n"""
              f"Thanks, {self.name}, for your purchase!")
        general = shop.purchase(self.product_cart)
        print("You have bought:")
        for product, cost in general.items():
            print(f"{self.product_cart[product]} "
                  f"{product}s for {cost:.2f} dollars")
        print(f"Total cost is {sum(general.values()):.2f} dollars\n"
              f"See you again!\n")
