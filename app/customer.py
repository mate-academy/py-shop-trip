from typing import List, Dict, Any

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        products: Dict[str, int | float],
        location: List[int | float],
        money: int | float,
        car: Car,
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def get_customers_list(data: dict) -> List:
        customers = []
        for customer in data["customers"]:
            products_list = {
                name: quantity
                for name, quantity in customer["product_cart"].items()
            }
            customer_instance = Customer(
                name=customer["name"],
                products=products_list,
                location=customer["location"],
                money=customer["money"],
                car=Car(**customer["car"]),
            )
            customers.append(customer_instance)
        return customers

    def find_the_cheapest_shop(
        self, shops: List[Shop], fuel_price: float
    ) -> Any:
        distances = {}
        for shop in shops:
            trip_fuel_cost = Car.calculate_trip_cost(
                customer=self, shop=shop, fuel_price=fuel_price
            )
            bill = self.bill_total(shop, True)
            trip_cost = round(trip_fuel_cost + bill, 2)
            distances[trip_cost] = shop
        cheapest_shop_cost = min(distances.keys())
        cheapest_shop_instance = distances[cheapest_shop_cost]

        return cheapest_shop_instance, cheapest_shop_cost, distances

    def go_shopping(
        self,
        cheapest_shop: Shop,
        cheapest_cost: float,
        distance_to_shops: dict,
    ) -> bool:
        print(f"{self.name} has {self.money} dollars")
        for price, shop in distance_to_shops.items():
            print(f"{self.name}'s trip to the {shop.name} costs {price}")
        if cheapest_cost > self.money:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return False
        print(f"{self.name} rides to {cheapest_shop.name}")
        cheapest_shop.make_purchase(customer=self, cost=cheapest_cost)
        return True

    def go_home(self) -> None:
        print(
            f"{self.name} rides home\n{self.name} "
            f"now has {self.money} dollars\n"
        )

    def bill_total(self, shop: Shop, total: bool) -> Any:
        product_prices_in_bill = {}
        for products_in_cart, quantity in self.products.items():
            product_prices_in_bill[products_in_cart] = (
                shop.products[products_in_cart] * quantity
            )
        bill = sum(product_prices_in_bill.values())
        if total:
            return bill
        return product_prices_in_bill
