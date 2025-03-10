from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            customer: dict
    ) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"])

    def _get_product_cost(
            self,
            shop: Shop
    ) -> int | float:
        return shop.calculate_products_cost(self.product_cart)

    def _get_fuel_cost(
            self,
            fuel_price: int | float,
            shop_location: list,
            car: Car
    ) -> int | float:
        return car.calculate_fuel_cost(
            fuel_price,
            self.location, shop_location
        )

    def _calculate_trip_cost(
            self,
            fuel_price: int | float,
            shop: Shop,
            car: Car
    ) -> int | float:
        product_cost = self._get_product_cost(shop)
        fuel_cost = self._get_fuel_cost(fuel_price, shop.location, car)

        return product_cost + fuel_cost

    def trip(
            self,
            shops: list,
            fuel_price: int | float
    ) -> None:
        print(f"{self.name} has {self.money} dollars")

        cheaper_shop = None
        cheaper_shop_cost = float("inf")

        for shop in shops:
            new_shop = Shop(shop)
            cost = self._calculate_trip_cost(fuel_price, new_shop, self.car)
            print(f"{self.name}'s trip to the {new_shop.name} costs {cost}")
            if cost >= cheaper_shop_cost:
                continue
            cheaper_shop_cost = cost
            cheaper_shop = new_shop

        if self.money < cheaper_shop_cost:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return
        print(f"{self.name} rides to {cheaper_shop.name}")
        print("")

        cheaper_shop.receipt(self)

        self.money -= cheaper_shop_cost

        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars")
        print("")
