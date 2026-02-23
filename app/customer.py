from app.car import Car
from math import sqrt


class Customer:
    def __init__(self, name: str,
                 wanted_products: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.wanted_products = wanted_products
        self.location = location
        self.money = money
        self.car = car

    def get_distance(self, shop: type) -> float:
        cust_location = self.location
        shop_location = shop.location
        x1 = cust_location[0]
        y1 = cust_location[1]
        x2 = shop_location[0]
        y2 = shop_location[1]
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def get_price(self, shop: type, fuel_price: float) -> float:
        distance = self.get_distance(shop)
        result = (((distance / 100) * self.car.fuel_consumption) * fuel_price)
        return result * 2

    def buy_cost(self, shop: type) -> float:
        cost = 0

        for product, amount in self.wanted_products.items():
            price = shop.products_available.get(product)

            if price is not None:
                cost += amount * price

        return cost

    def trip_cost(self, shop: type, fuel_price: float) -> float:
        fuel = self.get_price(shop, fuel_price)
        products = self.buy_cost(shop)
        return round(fuel + products, 2)

    def printer(self, list_shops: list, fuel: float) -> None:
        customer = self
        print(f"{customer.name} has {customer.money} dollars")
        for shop in list_shops:
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs "
                  f"{customer.trip_cost(shop, fuel)}")

    def cheapest(self, list_shops: list, fuel: float) -> type:
        cheapest_shop = list_shops[0]
        cheapest = self.trip_cost(cheapest_shop, fuel)
        for shop in list_shops[1:]:
            shop_cost = self.trip_cost(shop, fuel)
            if shop_cost < cheapest:
                cheapest = shop_cost
                cheapest_shop = shop
        return cheapest_shop

    def buy_at_shop(self, shop: type) -> None:
        final = 0

        for product, amount in self.wanted_products.items():
            price = shop.products_available.get(product)

            if price is None:
                continue

            result = amount * price

            if result.is_integer():
                result = int(result)

            print(f"{amount} {product}s for {result} dollars")
            final += result

        print(f"Total cost is {final} dollars")
        print("See you again!")
