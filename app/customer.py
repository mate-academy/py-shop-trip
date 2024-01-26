from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_info: dict, car: Car) -> None:
        self.name = customer_info.get("name")
        self.product_list = customer_info.get("product_cart")
        self.location = customer_info.get("location")
        self.money = customer_info.get("money")
        self.car = car

    def choose_shop(self, shops: list) -> Shop | None:
        total_expenses = [
            round(shop.calculate_check(self.product_list, total_flag=True)
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

    def drives_to(self, shop: Shop) -> None:
        home_gps = self.location
        shop_gps = shop.location

        print(f"{self.name} rides to {shop.name}\n")

        self.location = shop_gps
        shop_expenses = shop.purchase_with_receipt(
            self.name,
            self.product_list
        )
        self.money -= (
            self.car.get_fuel_cost(home_gps, shop_gps)
            + shop_expenses
        )

        print(f"{self.name} rides home")
        self.location = home_gps

    def check_wallet(self) -> None:
        print(f"{self.name} now has {self.money} dollars\n")
