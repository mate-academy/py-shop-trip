import math
import datetime
from app.shop import Shop
from decimal import Decimal, getcontext, ROUND_HALF_UP
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
        self.money = Decimal(money)
        self.car = car
        Customer.list_customers.append(self)

    @staticmethod
    def fmt(x_num: int | float) -> str:
        return str(int(x_num)) if x_num == int(x_num) else str(x_num)

    def spend_money_for_trip(self) -> None | int | float | Shop:
        find_lower_trip = None
        shop_object = None
        total_fuel_price_trip = None
        total_cost_products = None

        # Checker if shop have products (Customer)
        for shop in Shop.list_shops:
            have_product = True
            for product in self.product_cart:
                if product not in shop.products:
                    have_product = False
                    break

            if not have_product:
                continue

        # Cost products price
            price_milk = (Decimal(self.product_cart["milk"])
                          * Decimal(shop.products["milk"]))
            price_bread = (Decimal(self.product_cart["bread"])
                           * Decimal(shop.products["bread"]))
            price_butter = (Decimal(self.product_cart["butter"])
                            * Decimal(shop.products["butter"]))
            sum_products_price = price_milk + price_bread + price_butter

        # Cost road price
            distance = Decimal(
                math.sqrt(
                    (shop.location[0] - self.location[0])
                    ** 2 + (shop.location[1] - self.location[1]) ** 2
                )
            )
            fuel_needed = distance * (Decimal(self.car["fuel_consumption"])
                                      / Decimal("100"))
            fuel_price = fuel_needed * Decimal(Customer.fuel_price)

            full_trip_price = round(2 * fuel_price + sum_products_price, 2)

            print(f"{self.name}'s trip to "
                  f"the {shop.name} costs {full_trip_price}")
            if find_lower_trip is None or full_trip_price < find_lower_trip:
                if self.money >= full_trip_price:
                    find_lower_trip = full_trip_price
                    shop_object = shop
                    total_fuel_price_trip = fuel_price * 2
                    total_cost_products = round(sum_products_price, 2)

        if shop_object is not None:
            print(f"{self.name} rides to {shop_object.name}")
            self.location = shop_object.location
            return (find_lower_trip,
                    shop_object,
                    total_fuel_price_trip,
                    total_cost_products
                    )

        return None, None, None, None

    @staticmethod
    def console_info() -> None:
        for customer in Customer.list_customers:
            print(f"{customer.name} has {customer.money} dollars")
            (find_lower_trip,
             shop_object,
             total_fuel_price_trip,
             sum_products_price
             ) = Customer.spend_money_for_trip(customer)
            if find_lower_trip is not None:
                today = datetime.datetime.now()
                formated_data = today.strftime("%d/%m/%Y %H:%M:%S")

                print("")
                print(f"Date: {formated_data}")
                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought:")

                # Cost only per 1 product
                only_milk_cost = (shop_object.products["milk"]
                                  * customer.product_cart["milk"])
                only_bread_cost = (shop_object.products["bread"]
                                   * customer.product_cart["bread"])
                only_butter_cost = (shop_object.products["butter"]
                                    * customer.product_cart["butter"])

                print(f'{customer.product_cart["milk"]} milks '
                      f'for {Customer.fmt(only_milk_cost)} dollars')
                print(f'{customer.product_cart["bread"]} breads '
                      f'for {Customer.fmt(only_bread_cost)} dollars')
                print(f'{customer.product_cart["butter"]} butters '
                      f'for {Customer.fmt(only_butter_cost)} dollars')
                print(f"Total cost is "
                      f"{sum_products_price.normalize()} dollars")
                print("See you again!")
                print("")
                print(f"{customer.name} rides home")
                customer.money -= sum_products_price + total_fuel_price_trip
                customer.money = (customer.money.quantize
                                  (Decimal("0.01"), rounding=ROUND_HALF_UP))
                print(f"{customer.name} now has {customer.money} dollars")
                print()

            else:
                print(f"{customer.name} doesn't have"
                      f" enough money to make a purchase in any shop")
        return
