import decimal
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list,
                 money: str, car_fuel_consumption: float):
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
        fuel_consumption = self.car_fuel_consumption
        distance = ((home_x - shop_x) ** 2 + (hone_y - shop_y) ** 2) ** 0.5
        round_trip = round(2 * distance, 2)
        trans_cost = fuel_consumption / 100 * round_trip * fuel_price
        return decimal.Decimal(round(trans_cost, 2))

    def shop_selection(self, fuel_price):
        print(f"{self.name} has {self.money} dollars")
        best_cost = None
        best_shop = None
        for shop in Shop.shops.values():
            transportation = self.transportation_cost(shop, fuel_price)
            products = shop.products_price(self.product_cart)
            costs = round((transportation + products), 2)
            print(f"{self.name}'s trip to the {shop.name} costs {costs}")
            if best_cost is None:
                best_cost = decimal.Decimal(costs)
                best_shop = shop.name
            if best_cost > decimal.Decimal(costs):
                best_cost = decimal.Decimal(costs)
                best_shop = shop.name
        if self.money >= best_cost:
            print(f"{self.name} rides to {best_shop}\n")
            self.cost = best_cost
            return best_shop
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")
            return None

    def buy_products(self, shop_name: str):
        best_shop = Shop.shops.get(shop_name)
        best_shop.sell_products(self.product_cart, self.name)
        self.location = best_shop.location

    def back_home(self):
        print(f"{self.name} rides home")
        self.location = self.home
        self.money -= self.cost
        print(f"{self.name} now has {self.money} dollars\n")
