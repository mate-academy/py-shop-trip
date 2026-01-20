import math
from app.shop import Shop


class Customer:
    def __init__(
            self,
            customer: dict
    ) -> None:
        self._name: str = customer["name"]
        self._product_cart: dict[str, int] = customer["product_cart"]
        self._location: list[int] = customer["location"]
        self._money: int = customer["money"]
        self._car: dict[str, int | str] = customer["car"]

    def calculate_cheapest_shop_and_price(self,
                                          shops: list[Shop],
                                          fuel_price: float
                                          ) -> tuple[Shop, float]:
        print(f"{self._name} has {self._money} dollars")

        cheapest_shop: Shop = None
        min_trip_cost = float("inf")
        for shop in shops:
            distance = math.sqrt(
                (self._location[0] - shop.location[0]) ** 2
                + (self._location[1] - shop.location[1]) ** 2
            )
            fuel_cost = (self._car["fuel_consumption"] / 100
                         * fuel_price * distance * 2)

            products_cost = 0
            for product, amount in self._product_cart.items():
                if product not in shop.products:
                    print(f"No {product} in shop")
                else:
                    products_cost += amount * shop.products.get(product, 0)

            trip_cost = fuel_cost + products_cost

            if trip_cost < min_trip_cost:
                min_trip_cost = trip_cost
                cheapest_shop = shop

            print(f"{self._name}'s trip to the {shop.name} "
                  f"costs {trip_cost:.2f}")

        return cheapest_shop, min_trip_cost

    def make_purchases(self,
                       shop: Shop,
                       trip_cost: float
                       ) -> bool:
        if trip_cost > self._money:
            print(f"{self._name} doesn't have enough money to "
                  f"make a purchase in any shop")
            return False

        print(f"{self._name} rides to {shop.name}\n\n"
              f"Date: 04/01/2021 12:33:41\n"
              f"Thanks, {self._name}, for your purchase!\n"
              f"You have bought:")

        total_cost = 0
        for product, amount in self._product_cart.items():
            if product not in shop.products:
                print(f"No {product} in shop")
            else:
                product_price = shop.products.get(product, 0) * amount
                formated_price = f"{product_price:.2f}".rstrip("0").rstrip(".")
                print(f"{amount} {product}s for {formated_price} dollars")
                total_cost += product_price

        self._money -= trip_cost
        print(f"Total cost is {round(total_cost, 2)} dollars\n"
              f"See you again!\n\n"
              f"{self._name} rides home\n"
              f"{self._name} now has {self._money:.2f} dollars\n")

        return True
