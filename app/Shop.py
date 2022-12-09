from app.Customer import Customer
import math


class Shop:
    def __init__(
        self,
        shop_name: str,
        location: dict,
        products: dict,
        person_name: str,
        person_cart: dict,
        person_location: list,
        person_money: int,
        person_car: dict,
        fuel_price: int,
    ) -> None:

        self.shop_name = shop_name
        self.location = location
        self.products = products
        self.person_name = person_name
        self.person_cart = person_cart
        self.person_location = person_location
        self.person_money = person_money
        self.person_car = person_car
        self.fuel_price = fuel_price

    def get_product_cost(self, product: str) -> str:
        return self.products[product]

    def get_fuel_price(self) -> int:
        car_consumption = self.person_car["fuel_consumption"]
        distance = math.dist(self.person_location, self.location)
        return round(distance * 2 / 100 * car_consumption * self.fuel_price, 2)

    def calculate(self, customer: Customer) -> int:
        cost_sum = 0
        for item in self.products:
            cost_sum += self.get_product_cost(item) * customer.get_count(item)
        return cost_sum

    def info_buy(self,
                 data: dict,
                 cheap_shop: str,
                 customer: Customer) -> None:
        total = 0
        for item in data:
            if item["name"] == cheap_shop:
                for product in item["products"]:
                    summary = \
                        customer.get_count(product) * item["products"][product]
                    total += summary
                    print(
                        f"{customer.get_count(product)} {product}s "
                        f"for {summary} dollars"
                    )
                print(f"Total cost is {total} dollars")
                print("See you again!\n")
