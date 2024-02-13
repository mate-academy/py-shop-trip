from datetime import datetime

from app.data.customers.cars.car import Car
from app.data.location import Location
from app.data.product_cart import ProductCart
from app.data.shops.shops import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = ProductCart(**product_cart)
        self.location = Location(*location)
        self.money = money
        self.car = Car(**car)

    def fuel_dist(self, shop: Shop) -> float:
        shop_loc = [self.location.x]
        cust_loc = [shop.location.x]
        shop_loc.append(self.location.y)
        cust_loc.append(shop.location.y)
        return (self.car.fuel_consumption
                * ((shop_loc[0] - cust_loc[0]) ** 2
                   + (shop_loc[1] - cust_loc[1]) ** 2) ** 0.5)

    def sales_receipt(self, cheapest_shop: Shop) -> None:
        date = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        print(f"{self.name} rides to {cheapest_shop.name}\n\n"
              f"Date: {date}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              f"You have bought:")
        price: int = 0
        for product, quantity in self.product_cart.products.items():
            product_cost = (quantity
                            * cheapest_shop.products_price.products[product])
            print(f"{quantity} {product}s for {product_cost:g} dollars")
            price += product_cost

        print(f"Total cost is {price:g} dollars\n"
              f"See you again!\n\n"
              f"{self.name} rides home\n"
              f"{self.name} now has {self.money:.2f} dollars\n")
