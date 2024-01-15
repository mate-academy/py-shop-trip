from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def make_shop_trip(self, shops: list, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        best_shop = None
        best_price = None
        for shop in shops:
            fuel_cost = self.car.calculate_fuel_price(
                self.location,
                shop.location,
                fuel_price
            )
            total_cost = (shop.get_prices(self.product_cart) + fuel_cost)
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {round(total_cost, 2)}")
            if not best_price or total_cost < best_price:
                best_price = total_cost
                best_shop = shop
        if self.money < best_price:
            print(f"{self.name} "
                  f"doesn't have enough money to make a purchase in any shop")
            return
        print(f"{self.name} rides to {best_shop.name}\n")
        best_shop.print_purchase_receipt(self)
        print(f"{self.name} rides home")
        self.money = round(self.money - best_price, 2)
        print(f"{self.name} now has {self.money} dollars\n")
