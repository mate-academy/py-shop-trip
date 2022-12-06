from app.Customer import Customer
import math


class Shop(Customer):
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
        super().__init__(
            person_name,
            person_cart,
            person_location,
            person_money,
            person_car,
            fuel_price,
        )
        self.shop_name = shop_name
        self.location = location
        self.products = products

    def get_product_cost(self, product: str) -> str:
        return self.products[product]

    def get_fuel_price(self) -> int:
        car_consumption = self.person_car["fuel_consumption"]
        distance = math.dist(self.person_location, self.location)
        return round(distance * 2 / 100 * car_consumption * self.fuel_price, 2)

    def calculate(self) -> int:
        cost_sum = 0
        for item in self.products:
            cost_sum += self.get_product_cost(item) * self.get_count(item)
        return cost_sum

    def info_buy(self, data: dict, cheap_shop: str) -> None:
        total = 0
        for item in data:
            if item["name"] == cheap_shop:
                for i in item["products"]:
                    summary = self.get_count(i) * item["products"][i]
                    total += summary
                    print(f"{self.get_count(i)} {i}s for {summary} dollars")
                print(f"Total cost is {total} dollars")
                print("See you again!\n")
