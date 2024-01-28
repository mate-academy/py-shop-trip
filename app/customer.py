from app.car import Car
from app.shop import Shop


class Customer:
    home = None
    in_shop = None

    def __init__(self, customer_info: dict, car: Car) -> None:
        self.name = customer_info.get("name")
        self.product_list = customer_info.get("product_cart")
        self.location = customer_info.get("location")
        self.money = customer_info.get("money")
        self.car = car

    def choose_shop(self, shops: list) -> Shop | None:
        total_expenses = [
            round(shop.calculate_check(self.product_list)
                  + self.car.get_fuel_cost(self.location, shop.location), 2)
            for shop in shops
        ]

        for i in range(len(total_expenses)):
            print(
                f"{self.name}'s trip to the {shops[i].name} "
                f"costs {total_expenses[i]}"
            )

        if min(total_expenses) <= self.money:
            index = total_expenses.index(min(total_expenses))
            return shops[index]
        return None

    def drive_to(self, shop: Shop) -> None:
        self.home = self.location
        self.in_shop = shop
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

    def buy_products(self) -> None:
        shop_expenses = self.in_shop.purchase_with_receipt(
            self.name,
            self.product_list
        )
        self.money -= shop_expenses

    def return_home(self) -> None:
        print(f"{self.name} rides home")
        self.money -= self.car.get_fuel_cost(self.location, self.home)
        self.location = self.home

    def check_wallet(self) -> None:
        print(f"{self.name} now has {self.money} dollars\n")
