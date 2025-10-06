import math
import datetime
from app.shop import Shop
from decimal import Decimal, getcontext
getcontext().prec = 6


class Customer:
    list_customers = []
    fuel_price = 0

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int | float,
                 car: dict
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        Customer.list_customers.append(self)

    def spend_money_for_trip(self) -> None | int | float | Shop:
        find_lower_trip = None
        shop_object = None
        fuel_price_r = None

        # Cost products price
        for shop in Shop.list_shops:
            price_milk = self.product_cart["milk"] * shop.products["milk"]
            price_bread = self.product_cart["bread"] * shop.products["bread"]
            price_butter = self.product_cart["butter"] * shop.products["butter"]
            sum_products_price = price_milk + price_bread + price_butter

        # Cost road price
            distance = math.sqrt((shop.location[0] - self.location[0]) ** 2
                                         + (shop.location[1]
                                            - self.location[1]) ** 2)
            fuel_needed = distance * self.car["fuel_consumption"] / 100
            fuel_price = fuel_needed * Customer.fuel_price

            price = 2 * fuel_price + sum_products_price
            if find_lower_trip is None or price < find_lower_trip:
                if self.money >= price:
                    find_lower_trip = price
                    shop_object = shop
                    fuel_price_r = fuel_price
            print(f"{self.name}'s trip to the {shop.name} costs {price:.2f}")

        if shop_object is not None:
            print(f"{self.name} rides to {shop_object.name}")
            return find_lower_trip, shop_object, fuel_price_r

        return None, None, None

    @staticmethod
    def console_info() -> None:
        for customer in Customer.list_customers:
            print(f"{customer.name} has {customer.money} dollars")
            (find_lower_trip, shop_object,
             fuel_price_r) = Customer.spend_money_for_trip(customer)
            if find_lower_trip is not None:
                today = datetime.datetime.now()
                formated_data = today.strftime("%d/%m/%Y %H:%M:%S")

                print("")
                print(f"Date: {formated_data}")
                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought:")
                cost_milk = (shop_object.products["milk"]
                             * customer.product_cart["milk"])
                cost_bread = (shop_object.products["bread"]
                              * customer.product_cart["bread"])
                cost_butter = (shop_object.products["butter"]
                               * customer.product_cart["butter"])
                total_cost = round(cost_milk + cost_bread + cost_butter, 2)
                print(f'{customer.product_cart["milk"]}'
                      f' milks for {cost_milk} dollars')
                print(f'{customer.product_cart["bread"]}'
                      f' breads for {cost_bread} dollars')
                print(f'{customer.product_cart["butter"]}'
                      f' butters for {cost_butter} dollars')
                print(f"Total cost is {total_cost} dollars")
                print("See you again!")
                print("")
                print(f"{customer.name} rides home")
                customer.money -= total_cost + fuel_price_r
                print(f"{customer.name} now has {customer.money} dollars")
                print()

            else:
                print(f"{customer.name} doesn't have"
                      f" enough money to make a purchase in any shop")
        return
