import math
import datetime


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_the_cost_of_products(self, shop):
        cost_of_products = 0
        for product in self.product_cart:
            cost_of_products += shop.products[product]\
                * self.product_cart[product]
        return round(cost_of_products, 2)

    def calculate_the_cost_of_road(self, shop, fuel_cost):

        distance = math.dist(self.location, shop.location)
        liter_per_km = self.car["fuel_consumption"] / 100
        cost_of_the_road = round((distance * liter_per_km * fuel_cost) * 2, 2)

        return cost_of_the_road

    def calc_the_cost_of_trip(self, shop, fuel_cost):
        cost_of_trip = self.calculate_the_cost_of_products(shop) \
            + self.calculate_the_cost_of_road(shop, fuel_cost)
        return cost_of_trip

    def choose_the_shop(self, shops: list, fuel_cost: int):

        print(f"{self.name} has {self.money} dollars")
        min_cost = self.calc_the_cost_of_trip(shops[0], fuel_cost)
        best_shop = shops[0]

        for shop in shops:

            cost = self.calc_the_cost_of_trip(shop, fuel_cost)
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")

            if cost < min_cost:
                min_cost = cost
                best_shop = shop

        if self.money > min_cost:
            print(f"{self.name} rides to {best_shop.name}\n")
            best_shop.purchase(self)
            self.money -= min_cost
            self.coming_home()
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")

    def coming_home(self):

        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")


class Shop:

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict):
        self.name = name
        self.location = location
        self.products = products

    def purchase(self, customer):
        print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        cost_of_products = 0
        for product in self.products:
            cost_of_product = customer.product_cart[product]\
                * self.products[product]
            cost_of_products += cost_of_product
            print(f"{customer.product_cart[product]} "
                  f"{product}s for {cost_of_product} dollars")
        print(f"Total cost is {cost_of_products} dollars")
        print("See you again!\n")