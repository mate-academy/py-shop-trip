from app.cars import Car
from app.shops import Shop


class Customer:
    customers = []

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.available_shops = []
        Customer.customers.append(self)
        self.check_shops()

    def do_shop_trip(self) -> None:
        print(f"{self.name} has {self.money} dollars")
        shops = {shop: self.calculate_costs(shop)
                 for shop in self.available_shops}
        cheaper_shop = min(shops, key=shops.get)

        if shops[cheaper_shop] <= self.money:
            print(f"{self.name} rides to {cheaper_shop}\n")
            self.money -= shops[cheaper_shop]
            return (cheaper_shop.print_bill(self.name, self.product_cart),
                    self.ride_home())

        else:
            print(f"{self.name} doesn't have enough money"
                  f" to make a purchase in any shop")

    def check_shops(self) -> None:
        self.available_shops = (
            [shop for shop in Shop.shops
             if set(self.product_cart).issubset(set(shop.products))]
        )

    def calculate_costs(self, shop: Shop) -> float:
        fuel = self.car.fuel_costs(self.location, shop.location)
        products = sum(shop.products[key] * self.product_cart[key]
                       for key in self.product_cart)
        costs = round(fuel + products, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {costs}")
        return costs

    def ride_home(self) -> None:
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")
