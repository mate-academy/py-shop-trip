from app.car import Car
from app.shop import ProductCart, Shop


class Customer:
    def __init__(self, name: str, product_cart: list[ProductCart],
                 location: list, money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def choose_trip(self, shops: list, fuel_price: float) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")
        min_cost = self.money + 1
        shop_for_trip = Shop("", [], [])
        for shop in shops:
            road_cost = (fuel_price
                         * self.car.calculate_required_fuel(self.location,
                                                            shop.location)
                         )
            cost_trip = round((road_cost
                               + shop.calculate_amount_purchase(self)), 2)
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {cost_trip}")
            if cost_trip < min_cost:
                min_cost = cost_trip
                shop_for_trip = shop
                cost_fuel = road_cost
        if min_cost <= self.money:
            print(f"{self.name} rides to {shop_for_trip.name}\n")
            self.money -= round(cost_fuel, 2)
            return shop_for_trip
        print(f"{self.name} doesn't have enough money",
              "to make a purchase in any shop")
        return None

    def go_to_the_shop(self, shop: Shop) -> None:
        home_location = self.location
        self.location = shop.location
        payment_by_check = shop.calculate_amount_purchase(self,
                                                          print_check=True)
        self.money -= payment_by_check
        print(f"{self.name} rides home\n"
              f"{self.name} now has {round(self.money, 2)} dollars\n")
        self.location = home_location
