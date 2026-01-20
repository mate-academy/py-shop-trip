import datetime

from app.car import Car
from app.location import Location
from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __repr__(self) -> str:
        return (f"Customer(name={self.name}, products={self.product_cart}, "
                f"location={self.location}, "
                f"money={self.money}, car={self.car})")

    def buy_products(self, current_shop: Shop) -> float:
        total_cost = 0
        for key, value in self.product_cart.items():
            cost = current_shop.products[key] * value
            cost = round(cost) if ".0" in str(cost) else cost
            print(f"{value} {key}s for {cost} dollars")
            total_cost += cost

        return total_cost

    def get_all_trip_costs(self, shops: list[Shop], fuel_price: float) -> dict:
        result_costs = {}
        print(f"{self.name} has {self.money} dollars")
        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            result_costs[shop] = trip_cost

        return result_costs

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop_and_home = Location.calculate_distance(
            shop_location=shop.location,
            customer_location=self.location
        )

        fuel_cost_to_shop_and_home = self.car.calculate_fuel_costs(
            distance_to_shop_and_home=distance_to_shop_and_home,
            fuel_price=fuel_price
        )

        product_cost_total = shop.total_cost_of_product_in_cart(
            product_cart=self.product_cart
        )

        # multiply means fuel costs to home and shop
        total_trip_cost = (product_cost_total
                           + (fuel_cost_to_shop_and_home * 2))

        return round(total_trip_cost, 2)

    def process_purchasing(self, current_shop: Shop, min_cost: float) -> None:
        print(f"{self.name} rides to {current_shop.name}")
        print()
        today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {today}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_cost = self.buy_products(current_shop)

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()

        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - min_cost} dollars")
        print()
