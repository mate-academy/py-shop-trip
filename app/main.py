import dataclasses
import datetime
import json
from typing import List


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    home_location: list # = location
    money: int
    car: dict
    fuel_price: float

    def fuel_cost(self, shop): #: Shop
        distance = ((self.location[0] - shop.location[0]) ** 2
                    + (self.location[1] - shop.location[1]) ** 2) ** 0.5
        return self.fuel_price * self.car["fuel_consumption"] * distance / 100

    def find_cheapest_shop_and_print_info(self, shops):  #: List[Shop]
        print(f"{self.name} has {self.money} dollars")
        the_cheapest = shops[0]
        for shop in shops:
            print(f"{self.name}'s trip to the {shop.name} costs {shop.trip_to_shop(self)}")
            if shop.trip_to_shop(self) < the_cheapest.trip_to_shop(self):
                the_cheapest = shop
        if the_cheapest.trip_to_shop(self) > self.money:
            print(f"{self.name} doesn't have enough money to make purchase in any shop")
        else:
            print(f"{self.name} rides to {the_cheapest.name}\n")
            self.location = the_cheapest.location
            the_cheapest.purchase_receipt(self)
            print(f"{self.name} rides home")
            self.location = self.home_location
            self.money -= the_cheapest.trip_to_shop(self)
            print(f"{self.name} now has {self.money} dollars\n")


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    def cost_of_all_products(self, customer: Customer):
        milk_cost = customer.product_cart["milk"] * self.products["milk"]
        bread_cost = customer.product_cart["bread"] * self.products["bread"]
        butter_cost = customer.product_cart["butter"] * self.products["butter"]
        total_cost = milk_cost + bread_cost + butter_cost
        return total_cost

    def trip_to_shop(self, customer: Customer):
        cost_of_trip_to_shop = self.cost_of_all_products(customer) + customer.fuel_cost(self) * 2
        return round(cost_of_trip_to_shop, 2)

    def purchase_receipt(self, customer: Customer):
        milk_cost = customer.product_cart["milk"] * self.products["milk"]
        bread_cost = customer.product_cart["bread"] * self.products["bread"]
        butter_cost = customer.product_cart["butter"] * self.products["butter"]
        total_cost = milk_cost + bread_cost + butter_cost

        # current = datetime.datetime.today()

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        print(f"{customer.product_cart['milk']} milks for {milk_cost} dollars")
        print(f"{customer.product_cart['bread']} breads for {bread_cost} dollars")
        print(f"{customer.product_cart['butter']} butters for {butter_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")


def shop_trip():
    with open("app\config.json") as file:
        data = json.load(file)
        shop_list = []
        for shop in data['shops']:
            shop_obj = Shop(shop['name'], shop['location'], shop['products'])
            shop_list.append(shop_obj)
        for customer in data['customers']:
            customer_obj = Customer(customer['name'], customer['product_cart'], customer['location'], customer['location'], customer['money'], customer['car'], data['FUEL_PRICE'])
            customer_obj.find_cheapest_shop_and_print_info(shop_list)


shop_trip()