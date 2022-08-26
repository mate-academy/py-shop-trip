import json
from time import localtime, strftime


class ShopTrip:
    def __init__(self, file_name):
        self.data = self.load_data_from_json(file_name)
        self.fuel_price = self.data['FUEL_PRICE']
        self.customers = []
        self.shops = []
        for customer in self.data["customers"]:
            self.customers.append(customer)
        for shop in self.data["shops"]:
            self.shops.append(shop)

    @staticmethod
    def load_data_from_json(file_name: str) -> dict:
        with open(file_name, "r") as f:
            return json.load(f)

    def cost_trip(self, customer, shop) -> float:
        dist_x = abs(shop['location'][0] - customer['location'][0])
        dist_y = abs(shop['location'][1] - customer['location'][1])
        distance = (dist_x ** 2 + dist_y ** 2) ** 0.5 * 2
        fuel_consumption = customer["car"]["fuel_consumption"]
        fuel_price_1_km = self.fuel_price * fuel_consumption / 100
        result = round(distance * fuel_price_1_km, 2)
        return result

    @staticmethod
    def cost_buy(customer, shop) -> float:
        result = 0
        for key in customer["product_cart"].keys():
            result += customer["product_cart"][key] * shop["products"][key]
        return round(result, 2)

    def shop_trips(self, customer):
        print(f"{customer['name']} has {customer['money']} dollars")
        min_cost = None
        best_shop = None
        for shop in self.shops:
            price_trip = self.cost_trip(customer, shop)
            price_buy = self.cost_buy(customer, shop)
            cost = price_trip + price_buy
            print(f"{customer['name']}'s trip to the "
                  f"{shop['name']} costs {cost}")
            if min_cost is None or cost < min_cost:
                best_shop = shop
                min_cost = cost
        if customer["money"] < min_cost:
            print(f"{customer['name']} "
                  f"doesn't have enough money to make purchase in any shop")
            return

        print(f"{customer['name']} rides to {best_shop['name']}")
        print()
        print(f"Date: {strftime('%Y/%m/%d %H:%M:%S', localtime())}")
        print(f"Thanks, {customer['name']}, for you purchase!")
        print("You have bought: ")
        for product, product_num in customer["product_cart"].items():
            print(f"{product_num} {product}s for "
                  f"{product_num * best_shop['products'][product]} dollars")
        print(f"Total cost is {self.cost_buy(customer, best_shop)} dollars")
        print("See you again!")
        print()
        print(f"{customer['name']} rides home")
        print(f"{customer['name']} now has "
              f"{customer['money'] - min_cost} dollars")
        print()

    def all_customers_trip(self):
        for customer in self.customers:
            self.shop_trips(customer)
