from datetime import datetime
from decimal import Decimal

from _decimal import ROUND_DOWN

from app.car import Car
from app.fuel import Fuel
from app.product_cart import ProductCart
from app.shop import Shop


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: ProductCart,
            location: list,
            money: Decimal,
            car: Car,
            fuel: Fuel
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.fuel = fuel
        self.cost_trip = 0
        self.shop = None

    def calc_distance_to_shop(self, shop: Shop) -> float:
        return (
            round(((shop.location[0] - self.location[0]) ** 2
                   + (shop.location[1] - self.location[1]) ** 2) ** 0.5, 2)
        )

    def calc_cost_fuel_trip_to_shop(self, shop: Shop) -> Decimal:
        distance_to_shop = self.calc_distance_to_shop(shop)
        fuel_consumption_per_km = distance_to_shop / 100
        price_fuel = fuel_consumption_per_km * float(
            self.car.fuel_consumption) * float(self.fuel.price)
        return Decimal(price_fuel)

    def calc_minimal_cost_trip_to_shops(self, shops: list[Shop]) -> None:
        trip_to_shop = {}
        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            cost_trip_fuel = self.calc_cost_fuel_trip_to_shop(shop) * 2
            total_cost_products = self.get_total_cost_products(shop)
            cost_trip = (cost_trip_fuel + total_cost_products).quantize(
                Decimal("0.01"), rounding=ROUND_DOWN)
            print(f"{self.name}'s trip to the {shop.name} costs {cost_trip}")
            trip_to_shop[shop.name] = cost_trip

        affordable_shops = {
            name_shop: cost for name_shop, cost in
            trip_to_shop.items() if cost <= self.money
        }

        if not affordable_shops:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        self.cost_trip = min(affordable_shops.values())
        min_cost_shop = min(affordable_shops, key=affordable_shops.get)
        self.shop = [shop for shop in shops if shop.name == min_cost_shop][0]
        print(f"{self.name} rides to {min_cost_shop}\n")

        if self.shop is not None:
            print(self.print_order_receipt(self.shop))
            print(self.rides_home())

    def get_total_cost_products(self, shop: Shop) -> Decimal:
        total_cost_products = Decimal(0)
        for product in shop.products:
            total_price_product = (
                product.price
                * self.product_cart.get_quantity_products(product.name)
            )
            total_cost_products += total_price_product
        return total_cost_products

    def print_order_receipt(
            self,
            shop: Shop
    ) -> str:
        time_stamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        total_cost = 0
        order_receipt = (
            f"Date: {time_stamp}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought: \n"
        )
        for product_name, quantity in self.product_cart.entries.items():
            order_receipt += (f"{quantity} {product_name} for "
                              f"{shop.get_product_price(product_name)
                                 * quantity} dollars\n")
            total_cost += (shop.get_product_price(product_name) * quantity)

        order_receipt += (f"Total cost is "
                          f"{total_cost} dollars\nSee you again!\n")
        return order_receipt

    def rides_home(self) -> str:
        return (f"{self.name} rides home\n"
                f"{self.name} now has {self.money - self.cost_trip} dollars\n")
