import math


from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def fuel_costs(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        fuel_costs = 2 * (distance * self.car.fuel_consumption
                          / 100 * fuel_price)
        return round(fuel_costs, 2)

    def milk_costs(self, shop: Shop) -> float:
        return self.product_cart["milk"] * shop.products["milk"]

    def bread_costs(self, shop: Shop) -> float:
        return self.product_cart["bread"] * shop.products["bread"]

    def butter_costs(self, shop: Shop) -> float:
        return self.product_cart["butter"] * shop.products["butter"]

    def products_costs(self, shop: Shop) -> float:
        all_costs = self.milk_costs(shop) \
            + self.butter_costs(shop) + self.bread_costs(shop)
        return all_costs

    def shop_prints(self, shop: Shop) -> None:
        print("Date: 04/01/2021 12:33:41")
        # print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        print(f"{self.product_cart['milk']} milks "
              f"for {self.milk_costs(shop)} dollars")
        print(f"{self.product_cart['bread']} breads "
              f"for {self.bread_costs(shop)} dollars")
        print(f"{self.product_cart['butter']} butters "
              f"for {self.butter_costs(shop)} dollars")
        print(f"Total cost is {self.products_costs(shop)} dollars")
        print("See you again!\n")

    def money_after_shopping(self, shop: Shop, fuel_price: float) -> None:
        current_money = self.money - self.products_costs(shop) \
            - self.fuel_costs(shop, fuel_price)
        print(f"{self.name} now has {current_money} dollars\n")
