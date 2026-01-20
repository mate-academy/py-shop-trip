from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, money: float, location: list,
                 car: Car, product_cart: dict) -> None:
        self.name = name
        self.money = money
        self.location = [location[0], location[1]]
        self.car = car
        self.product_cart = product_cart

    def check_shopping_cost(self, shop: Shop, fuel_cost: float) -> float:
        distance = Car.get_distance(self.location, shop.location) * 2
        trip_cost = round(self.car.get_consumption_for_the_trip(
            distance) * fuel_cost, 2)

        products_cost = shop.calculate_purchase_cost(self.product_cart)

        return trip_cost + products_cost

    def find_the_cheapest_shopping(self, shops: list[Shop],
                                   fuel_price: float) -> (Shop, float):
        chosen_shop = None
        cheapest_cost = None

        for shop in shops:
            shopping_cost = self.check_shopping_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} "
                  + f"costs {shopping_cost}")

            if not cheapest_cost or shopping_cost < cheapest_cost:
                cheapest_cost = shopping_cost
                chosen_shop = shop

        return chosen_shop, cheapest_cost

    def make_shopping(self, shop: Shop, fuel_price: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.car.move_to_destination(shop.location)

        products_cost = shop.make_purchase(self.product_cart, self.name)

        print(f"{self.name} rides home")
        self.car.move_to_destination(self.location)

        fuel_spent = self.car.finish_trip()

        transportation_cost = round(fuel_spent * fuel_price, 2)

        self.money -= (products_cost + transportation_cost)
        print(f"{self.name} now has {self.money} dollars\n")
