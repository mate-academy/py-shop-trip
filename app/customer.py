import decimal
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list, money: str, car_fuel_consumption: float):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = decimal.Decimal(money)
        self.car_fuel_consumption = car_fuel_consumption
        self.home = location
        self.cost = 0

    def transportation_cost(self, shop: Shop, fuel_price):
        shop_x, shop_y = shop.location[0], shop.location[1]
        home_x, hone_y = self.location[0], self.location[1]
        distance = 2 * (((home_x - shop_x) ** 2 + (hone_y - shop_y) ** 2) ** 0.5)
        transport_cost = decimal.Decimal(self.car_fuel_consumption / 100 * distance * fuel_price)
        return transport_cost

    def shop_selection(self, fuel_price):
        alternatives = {}
        for shop in Shop.shops.values():
            costs = shop.products_price(self.product_cart) + self.transportation_cost(shop, fuel_price)
            alternatives[shop.name] = decimal.Decimal(costs)
            print(f"{self.name}'s trip to the {shop.name} costs {costs}")
        chip_shop_name = min(alternatives, key=alternatives.get)
        if self.money >= alternatives[chip_shop_name]:
            print(f"{self.name} rides to {chip_shop_name}")
            self.cost = alternatives[chip_shop_name]
            return chip_shop_name
        else:
            print(f"{self.name} doesn't have enough money to make purchase in any shop")
            return 0

    def buy_products(self, chip_shop_name):
        current_shop = Shop.shops.get(chip_shop_name, 0)
        if isinstance(current_shop, Shop):
            current_shop.sell_products(self.product_cart, self.name)
        self.location = current_shop.location

    def back_home(self):
        self.location = self.home
        self.money -= self.cost
        print(f"{self.name} now has {self.money} dollars")
