from app.car import Car
from app.shop import Shop
import datetime


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict[str, int],
                 location: list[int],
                 money: int | float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.cheaper_shop: Shop = None
        self.cost_to_shop = None

    def cost_way_to_shop(self, shop: Shop, fuel_price: float) -> float:
        return self.car.cost_way(self.location, shop.location, fuel_price)

    def get_cost_products(self, shop: Shop) -> int:
        total = 0
        for product in self.product_cart:
            total += (shop.products[product] * self.product_cart[product])
        return total

    def get_trip_cost_to_shop(self, shop: Shop, fuel_price: float) -> float:
        cost = (self.cost_way_to_shop(shop, fuel_price) * 2
                + self.get_cost_products(shop))
        if self.cost_to_shop is not None:
            if cost < self.cost_to_shop:
                self.cost_to_shop = cost
                self.cheaper_shop = shop
        else:
            self.cost_to_shop = cost
            self.cheaper_shop = shop
        return cost

    def print_check(self) -> None:
        self.location = self.cheaper_shop.location

        time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time_now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for product in self.product_cart:
            cost_of_product = (self.cheaper_shop.products[product]
                               * self.product_cart[product])
            if cost_of_product == int(cost_of_product):
                cost_of_product = int(cost_of_product)

            print(f"{self.product_cart[product]}"
                  f" {product}s for"
                  f" {round(cost_of_product, 2)}"
                  f" dollars")
        print(f"Total cost is "
              f"{round(self.get_cost_products(self.cheaper_shop), 2)} dollars")
        print("See you again!\n")


def create_customers_from_list(customers_list: list[dict]
                               ) -> list[Customer]:
    customers = []
    for customer in customers_list:
        car = Car(customer["car"]["brand"],
                  customer["car"]["fuel_consumption"])
        customers.append(Customer(customer["name"],
                                  customer["product_cart"],
                                  customer["location"],
                                  customer["money"],
                                  car))

    return customers
