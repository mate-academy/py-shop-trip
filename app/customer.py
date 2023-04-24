import dataclasses

from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    home_location: list[int]
    money: int
    car: dict
    money_spent: int | float = 0
    current_location: list[int] = None

    def choose_shop_or_stay_home(
            self,
            shops_list: list[Shop],
            fuel_price: float
    ) -> None | Shop:
        self.current_location = self.home_location
        print(f"{self.name} has {self.money} dollars")
        calculated_trips = dict()
        for shop in shops_list:
            calculated_trips[
                self.calculate_trip_to_shop
                (
                    shop,
                    fuel_price
                )
            ] = shop
        cheapest_trip = min(calculated_trips.keys())
        if self.money < cheapest_trip:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return
        shop_to_choose = calculated_trips[cheapest_trip]
        print(f"{self.name} rides to {shop_to_choose.name}\n")
        self.money_spent = cheapest_trip
        self.current_location = shop_to_choose.location
        return shop_to_choose

    def calculate_trip_to_shop(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        x1 = self.home_location[0]
        y1 = self.home_location[1]
        x2 = shop.location[0]
        y2 = shop.location[1]
        total_distance = round(
            (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5) * 2,
            2
        )
        trip_fuel_consumption = \
            total_distance * self.car["fuel_consumption"] \
            / 100
        fuel_expenses = trip_fuel_consumption * fuel_price
        product_expenses = 0
        for product, amount_to_buy in self.product_cart.items():
            product_expenses += amount_to_buy * shop.products[product]
        trip_expenses = round(fuel_expenses + product_expenses, 2)
        print(f"{self.name}'s trip "
              f"to the {shop.name} costs {trip_expenses}")
        return trip_expenses

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.current_location = self.home_location
        print(f"{self.name} now has {self.money - self.money_spent} dollars\n")
