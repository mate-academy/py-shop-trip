import math
from typing import Union


class CostCalculation:
    def __init__(
            self,
            customers: dict,
            shops: dict,
            fuel_price: Union[int, float]
    ) -> None:
        self.customers = customers
        self.shops = shops
        self.fuel_price = fuel_price

    def calculation(self) -> None:

        for customer in self.customers.values():

            best_deal = float("inf")
            best_shop = None

            print(f"{customer.name} has {customer.money} dollars")

            for shop in self.shops.values():
                products_cost = 0
                fuel_costs = (
                    (self.fuel_price * customer.car["fuel_consumption"])
                    / 100 * math.dist(customer.location, shop.location)
                    * 2
                )

                for product in customer.product_cart.items():
                    if product[0] in shop.products:
                        products_cost += (
                            shop.products[product[0]] * product[1]
                        )
                    else:
                        products_cost = best_deal + 1
                trip_total_cost = fuel_costs + products_cost
                print(f"{customer.name}'s trip to the {shop.name} "
                      f"costs {round(trip_total_cost, 2)}")

                if trip_total_cost < best_deal:
                    best_deal = trip_total_cost
                    best_shop = shop

            the_rest_of_money = round(customer.money - best_deal, 2)
            if the_rest_of_money < 0:
                print(f"{customer.name} doesn't have enough money to "
                      f"make a purchase in any shop")
                break

            home_location = customer.location
            print(f"{customer} rides to {best_shop}\n")
            best_shop.sale_of_goods(customer)
            print(f"{customer} rides home")
            customer.location = home_location
            print(f"{customer} now has {the_rest_of_money} dollars\n")